"""Read literal manuscript inputs and active citations, preserving source locations.

This is a deliberately bounded source scanner, not a TeX interpreter. It handles
comments, nested iftrue/iffalse and newif flags, literal input/include paths,
includeonly, verbatim/comment environments, macro definitions and multiline
natbib citations. Unknown conditionals and dynamic inputs fail closed; citations
hidden in macro definitions are rejected rather than silently counted. The
compiled aux/bbl comparison remains a separate, required check.
"""
from __future__ import annotations

import bisect
import hashlib
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path


class ScanError(ValueError):
    pass


def blank(value: str) -> str:
    return "".join("\n" if c == "\n" else " " for c in value)


def strip_comments(text: str) -> str:
    """Keep offsets; percent is escaped iff preceded by an odd number of slashes."""
    chars = list(text)
    pos = 0
    while pos < len(text):
        if text[pos] == "\\":
            token = re.match(r"\\([A-Za-z@]+|.)", text[pos:], re.S)
            if token:
                name = token.group(1)
                cursor = pos + token.end()
                if name == "verb":
                    cursor += text[cursor:cursor + 1] == "*"
                    delimiter = text[cursor:cursor + 1]
                    end = text.find(delimiter, cursor + 1) if delimiter else -1
                    if end < 0:
                        raise ScanError(f"Unclosed verb near offset {pos}")
                    pos = end + 1
                    continue
                if name == "begin":
                    env = re.match(r"\s*\{(verbatim\*?|lstlisting|minted|comment)\}", text[cursor:])
                    if env:
                        closer = "\\end{" + env.group(1) + "}"
                        end = text.find(closer, cursor + env.end())
                        if end < 0:
                            raise ScanError(f"Unclosed {env.group(1)} near offset {pos}")
                        pos = end + len(closer)
                        continue
                pos = cursor
                continue
        if text[pos] != "%":
            pos += 1
            continue
        n = 0
        p = pos - 1
        while p >= 0 and text[p] == "\\":
            n += 1
            p -= 1
        if n % 2 == 0:
            end = text.find("\n", pos)
            end = len(text) if end < 0 else end
            chars[pos:end] = blank(text[pos:end])
            pos = end
        else:
            pos += 1
    return "".join(chars)


def group(text: str, pos: int, opening: str = "{", closing: str = "}") -> tuple[str, int]:
    while pos < len(text) and text[pos].isspace():
        pos += 1
    if pos >= len(text) or text[pos] != opening:
        raise ScanError(f"Expected {opening!r} near offset {pos}")
    start, depth, pos = pos + 1, 1, pos + 1
    while pos < len(text):
        if text[pos] == "\\":
            pos += 2
            continue
        if text[pos] == opening:
            depth += 1
        elif text[pos] == closing:
            depth -= 1
            if depth == 0:
                return text[start:pos], pos + 1
        pos += 1
    raise ScanError(f"Unclosed {opening!r} at offset {start - 1}")


CITE_NAMES = {"cite", "citep", "citet", "citeauthor", "citeyear", "citeyearpar",
              "citealp", "citealt", "citenum", "Citep", "Citet", "Citealp", "Citealt"}
TOKEN = re.compile(r"\\([A-Za-z@]+|.)", re.S)


@dataclass
class Citation:
    command_id: str
    file: str
    line: int
    end_line: int
    offset: int
    command: str
    keys: list[str]
    raw_command: str
    original_sentence: str
    context: str
    section: str
    kind: str


@dataclass
class ScanResult:
    main: str
    files: list[dict] = field(default_factory=list)
    citations: list[Citation] = field(default_factory=list)
    nocite_keys: list[str] = field(default_factory=list)
    excluded_ranges: list[dict] = field(default_factory=list)
    active_texts: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)


class Scanner:
    def __init__(self, root: Path, main: str = "manuscript.tex"):
        self.root = root.resolve()
        self.result = ScanResult(main)
        self.flags: dict[str, bool] = {}
        self.stack: list[dict] = []
        self.includeonly: set[str] | None = None
        self.visiting: list[Path] = []
        self.section = "Front matter"

    @property
    def active(self) -> bool:
        return all(f["value"] for f in self.stack)

    def scan(self) -> ScanResult:
        self._file(self.root / self.result.main)
        if self.stack:
            raise ScanError(f"Unclosed conditional: {self.stack[-1]}")
        return self.result

    def _file(self, path: Path) -> None:
        path = path.resolve()
        if not path.is_relative_to(self.root):
            raise ScanError(f"Input outside manuscript root: {path}")
        if path in self.visiting:
            raise ScanError(f"Recursive input: {path}")
        if not path.exists():
            raise ScanError(f"Missing active input: {path}")
        self.visiting.append(path)
        raw_bytes = path.read_bytes()
        raw = raw_bytes.decode("utf-8-sig").replace("\r\n", "\n")
        rel = path.relative_to(self.root).as_posix()
        text = strip_comments(raw)
        visible = list(text)
        newlines = [-1] + [m.start() for m in re.finditer("\n", raw)]
        line = lambda p: bisect.bisect_left(newlines, p)
        self.result.files.append({"file": rel, "sha256": hashlib.sha256(raw_bytes).hexdigest()})
        pending: list[Citation] = []

        def mask(a: int, b: int, reason: str = "") -> None:
            visible[a:b] = blank(text[a:b])
            if reason:
                self.result.excluded_ranges.append({"file": rel, "start_line": line(a),
                    "end_line": line(max(a, b - 1)), "reason": reason})

        pos = 0
        while match := TOKEN.search(text, pos):
            start, pos, name = match.start(), match.end(), match.group(1)
            if not self.active:
                mask(0 if start == 0 else last_end, start)
            last_end = pos
            if name in {"iftrue", "iffalse"} or name in self.flags:
                value = name == "iftrue" if name in {"iftrue", "iffalse"} else self.flags[name]
                self.stack.append({"value": value, "original": value, "else": False,
                                   "file": rel, "line": line(start)})
                mask(start, pos)
                continue
            if name == "else":
                if not self.stack or self.stack[-1]["else"]:
                    raise ScanError(f"Unexpected else at {rel}:{line(start)}")
                self.stack[-1]["value"] = not self.stack[-1]["original"]
                self.stack[-1]["else"] = True
                mask(start, pos)
                continue
            if name == "fi":
                if not self.stack:
                    raise ScanError(f"Unexpected fi at {rel}:{line(start)}")
                frame = self.stack.pop()
                if not frame["original"] and not frame["else"]:
                    self.result.excluded_ranges.append({"file": frame["file"],
                        "start_line": frame["line"], "end_line": line(start), "reason": "iffalse/false flag"})
                mask(start, pos)
                continue
            # A newif declaration contains an if token that must not open a branch.
            if name == "newif":
                flag = TOKEN.match(text, pos + len(text[pos:]) - len(text[pos:].lstrip()))
                if not flag or not flag.group(1).startswith("if"):
                    raise ScanError(f"Unsupported newif at {rel}:{line(start)}")
                if self.active:
                    self.flags[flag.group(1)] = False
                pos = last_end = flag.end()
                mask(start, pos)
                continue
            if name.startswith("if"):
                raise ScanError(f"Unsupported conditional \\{name} at {rel}:{line(start)}; compile/extend scanner first")
            if not self.active:
                mask(start, pos)
                continue
            if "if" + name.removesuffix("true").removesuffix("false") in self.flags and name.endswith(("true", "false")):
                self.flags["if" + name.removesuffix("true").removesuffix("false")] = name.endswith("true")
                mask(start, pos)
            elif name == "verb":
                if pos < len(text) and text[pos] == "*":
                    pos += 1
                delim = text[pos:pos + 1]
                end = text.find(delim, pos + 1) if delim else -1
                if end < 0:
                    raise ScanError(f"Unclosed verb at {rel}:{line(start)}")
                pos = last_end = end + 1
                mask(start, pos, "verbatim")
            elif name == "begin":
                env, end = group(text, pos)
                if env in {"verbatim", "verbatim*", "lstlisting", "minted", "comment"}:
                    closer = "\\end{" + env + "}"
                    close = text.find(closer, end)
                    if close < 0:
                        raise ScanError(f"Unclosed {env} at {rel}:{line(start)}")
                    pos = last_end = close + len(closer)
                    mask(start, pos, env)
            elif name in {"newcommand", "renewcommand", "providecommand", "DeclareRobustCommand", "def", "gdef", "edef", "xdef"}:
                cursor = pos
                if text[cursor:cursor + 1] == "*":
                    cursor += 1
                while text[cursor:cursor + 1].isspace():
                    cursor += 1
                if text[cursor:cursor + 1] == "{":
                    _, cursor = group(text, cursor)
                else:
                    macro = TOKEN.match(text, cursor)
                    if not macro:
                        raise ScanError(f"Unsupported macro definition at {rel}:{line(start)}")
                    cursor = macro.end()
                if name in {"def", "gdef", "edef", "xdef"}:
                    cursor = text.find("{", cursor)
                else:
                    while True:
                        while text[cursor:cursor + 1].isspace():
                            cursor += 1
                        if text[cursor:cursor + 1] != "[":
                            break
                        _, cursor = group(text, cursor, "[", "]")
                body, end = group(text, cursor)
                if re.search(r"\\(?:cite\w*|input|include|if\w*)\b", body):
                    raise ScanError(f"Dynamic citation/input/conditional in macro at {rel}:{line(start)}")
                pos = last_end = end
                mask(start, pos, "macro definition")
            elif name == "xpatchbibmacro":
                # Five balanced arguments patch a bibliography macro; their
                # deferred conditionals do not branch the manuscript source.
                # Still reject hidden citations or dynamic source inclusion.
                arguments = []
                cursor = pos
                for _ in range(5):
                    value, cursor = group(text, cursor)
                    arguments.append(value)
                if any(re.search(r"\\(?:cite\w*|input|include)\b", value) for value in arguments):
                    raise ScanError(f"Dynamic citation/input in bibliography patch at {rel}:{line(start)}")
                pos = last_end = cursor
                mask(start, pos, "bibliography macro patch")
            elif name == "includeonly":
                values, pos = group(text, pos)
                self.includeonly = {v.strip().removesuffix(".tex") for v in values.split(",")}
                last_end = pos
            elif name in {"input", "include"}:
                cursor = pos
                while text[cursor:cursor + 1].isspace():
                    cursor += 1
                if text[cursor:cursor + 1] == "{":
                    target, pos = group(text, cursor)
                else:
                    target_match = re.match(r"[^\s{}%]+", text[cursor:])
                    if not target_match:
                        raise ScanError(f"Unsupported input at {rel}:{line(start)}")
                    target = target_match.group()
                    pos = cursor + len(target)
                if re.search(r"[\\#]", target):
                    raise ScanError(f"Dynamic input at {rel}:{line(start)}")
                last_end = pos
                mask(start, pos)
                if name == "include" and self.includeonly is not None and target.removesuffix(".tex") not in self.includeonly:
                    continue
                # Plain TeX resolves relative inputs from the compilation cwd,
                # not from the directory of the currently read child file.
                child = self.root / target
                if not child.suffix:
                    child = child.with_suffix(".tex")
                self._file(child)
            elif name in {"section", "subsection", "subsubsection"}:
                cursor = pos + (text[pos:pos + 1] == "*")
                while text[cursor:cursor + 1].isspace():
                    cursor += 1
                if text[cursor:cursor + 1] == "[":
                    _, cursor = group(text, cursor, "[", "]")
                self.section, _ = group(text, cursor)
            elif name in CITE_NAMES or name == "nocite":
                cursor = pos + (text[pos:pos + 1] == "*")
                while True:
                    while text[cursor:cursor + 1].isspace():
                        cursor += 1
                    if text[cursor:cursor + 1] != "[":
                        break
                    _, cursor = group(text, cursor, "[", "]")
                argument, end = group(text, cursor)
                keys = [re.sub(r"\s+", "", k) for k in argument.split(",") if k.strip()]
                if any(re.search(r"[\\{}#]", k) for k in keys):
                    raise ScanError(f"Dynamic citation key at {rel}:{line(start)}")
                if name == "nocite":
                    self.result.nocite_keys.extend(keys)
                else:
                    citation = Citation("", rel, line(start), line(end - 1), start,
                        name, keys, raw[start:end], "", "", self.section, "")
                    pending.append(citation)
                    self.result.citations.append(citation)
                pos = last_end = end
            elif name == "end":
                env, end = group(text, pos)
                if env == "document":
                    mask(end, len(text), "after end document")
                    pos = last_end = len(text)
                    break
        if not self.active:
            mask(locals().get("last_end", 0), len(text))
        active_text = "".join(visible)
        self.result.active_texts[rel] = active_text
        for citation in pending:
            citation.original_sentence, citation.context, citation.kind = citation_context(
                active_text, citation.offset, citation.offset + len(citation.raw_command))
        self.visiting.pop()


def citation_context(text: str, start: int, end: int) -> tuple[str, str, str]:
    """Return complete sentence, with a complete paragraph/row for interpretation."""
    left = list(re.finditer(r"\n\s*\n", text[:start]))
    lo = left[-1].end() if left else 0
    right = re.search(r"\n\s*\n", text[end:])
    hi = end + right.start() if right else len(text)
    context = text[lo:hi].strip()
    # Table rows are units of evidence, not grammatical sentences.
    table_begins = list(re.finditer(r"\\begin\{(?:tabular\*?|tabularx|longtable)\}", text[:start]))
    table_ends = list(re.finditer(r"\\end\{(?:tabular\*?|tabularx|longtable)\}", text[:start]))
    in_table = bool(table_begins and (not table_ends or table_begins[-1].start() > table_ends[-1].start()))
    if in_table:
        row_start = text.rfind("\\\\", lo, start)
        row_end = text.find("\\\\", end, hi)
        lo = row_start + 2 if row_start >= 0 else lo
        hi = row_end + 2 if row_end >= 0 else hi
        value = re.sub(r"\s+", " ", text[lo:hi]).strip()
        value = re.sub(r"^\\(?:toprule|midrule|hline)\s*", "", value)
        return value, re.sub(r"\s+", " ", context), "table_row"
    # Exclude decimal points and common abbreviations when finding sentences.
    boundaries = []
    for m in re.finditer(r"[.!?](?:[\"'’”)]*)\s+(?=[A-Z\\])", text[lo:hi]):
        prefix = text[lo:lo + m.start() + 1]
        if re.search(r"(?:\be\.g|\bi\.e|\bet al|\bvs|\bFig|\bSec|\bDr|\bMr)\.$", prefix):
            continue
        boundaries.append((lo + m.start(), lo + m.end()))
    sentence_lo = max([b for a, b in boundaries if b <= start] or [lo])
    sentence_hi = min([a + 1 for a, b in boundaries if a >= end] or [hi])
    return (re.sub(r"\s+", " ", text[sentence_lo:sentence_hi]).strip(),
            re.sub(r"\s+", " ", context), "prose")


def scan_manuscript(root: Path, main: str = "manuscript.tex") -> ScanResult:
    result = Scanner(root, main).scan()
    for n, citation in enumerate(result.citations, 1):
        citation.command_id = f"C{n:03d}"
    return result


def compiled_keys(root: Path, main: str = "manuscript.tex") -> dict:
    """Read existing compiler artifacts; never run TeX or modify the manuscript."""
    stem = Path(main).with_suffix("")
    artifact_root = root / "build/latex" if (root / "build/latex" / stem.with_suffix(".aux")).exists() else root
    aux_keys: list[str] = []
    aux_commands: list[list[str]] = []
    artifacts: list[dict] = []
    visited: set[Path] = set()

    def read_aux(path: Path) -> None:
        path = path.resolve()
        if path in visited:
            return
        if not path.is_relative_to(root.resolve()) or not path.exists():
            raise ScanError(f"Missing/out-of-root aux input: {path}")
        visited.add(path)
        data = path.read_bytes()
        artifacts.append({"file": path.relative_to(root).as_posix(), "sha256": hashlib.sha256(data).hexdigest()})
        text = strip_comments(data.decode("utf-8"))
        for m in re.finditer(r"\\(citation|@input)\s*\{([^}]+)\}", text):
            if m.group(1) == "@input":
                read_aux(artifact_root / m.group(2))
            else:
                values = [k.strip() for k in m.group(2).split(",") if k.strip()]
                aux_commands.append(values)
                aux_keys.extend(values)

    read_aux(artifact_root / stem.with_suffix(".aux"))
    bbl = artifact_root / stem.with_suffix(".bbl")
    data = bbl.read_bytes()
    artifacts.append({"file": bbl.relative_to(root).as_posix(), "sha256": hashlib.sha256(data).hexdigest()})
    text = strip_comments(data.decode("utf-8"))
    bbl_keys = []
    for m in re.finditer(r"\\bibitem\b", text):
        pos = m.end()
        while text[pos:pos + 1].isspace():
            pos += 1
        if text[pos:pos + 1] == "[":
            _, pos = group(text, pos, "[", "]")
        value, _ = group(text, pos)
        bbl_keys.append(value.strip())
    return {"aux_keys": sorted(set(aux_keys)), "aux_commands": aux_commands,
            "aux_key_occurrences": len(aux_keys), "bbl_keys": bbl_keys, "artifacts": artifacts}
