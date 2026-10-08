"""Regression tests for false positives/negatives in reference auditing."""
from pathlib import Path
from contextlib import contextmanager
from uuid import uuid4
import shutil
import unittest

from active_tex import ScanError, compiled_keys, scan_manuscript, strip_comments


@contextmanager
def fixture_directory():
    # Python 3.13's private Windows temp-directory ACLs are incompatible with
    # this workspace sandbox. Ordinary workspace directories avoid that issue.
    parent = Path(__file__).resolve().parents[1] / "tmp" / "reference_scan_tests"
    parent.mkdir(parents=True, exist_ok=True)
    target = (parent / uuid4().hex).resolve()
    target.mkdir()
    try:
        yield target
    finally:
        if not target.is_relative_to(parent.resolve()) or target == parent.resolve():
            raise RuntimeError("Unsafe fixture cleanup path")
        shutil.rmtree(target)


class ActiveTexTests(unittest.TestCase):
    def scan(self, main, extra=None):
        with fixture_directory() as directory:
            root = Path(directory)
            (root / "manuscript.tex").write_text(main, encoding="utf-8")
            for filename, text in (extra or {}).items():
                (root / filename).parent.mkdir(parents=True, exist_ok=True)
                (root / filename).write_text(text, encoding="utf-8")
            return scan_manuscript(root)

    def test_comments_escaped_percent_and_multiline_citations(self):
        result = self.scan(r"""\begin{document}
Visible \% text. % \citep{comment}
\citep[see][p.~2]{alpha,
% hiding this line must not hide the next key
 beta}
\\% \citep{also_comment}
\end{document}
\citep{after_end}
""")
        self.assertEqual([c.keys for c in result.citations], [["alpha", "beta"]])
        self.assertEqual((result.citations[0].line, result.citations[0].end_line), (3, 5))

    def test_nested_disabled_branches_and_else(self):
        result = self.scan(r"""\iffalse
\citep{old}\iftrue\citep{nested}\else\citep{nested_else}\fi
\else
\citep{live}\iffalse\citep{old2}\else\citep{live2}\fi
\fi""")
        self.assertEqual([c.keys for c in result.citations], [["live"], ["live2"]])

    def test_literal_inputs_only_and_traversal_order(self):
        result = self.scan(r"\cite{first}\input{child}\cite{last}\iffalse\input{missing}\fi",
            {"child.tex": r"\cite{inside}", "history.tex": r"\cite{never_included}"})
        self.assertEqual([c.keys for c in result.citations], [["first"], ["inside"], ["last"]])
        self.assertEqual({f["file"] for f in result.files}, {"manuscript.tex", "child.tex"})

    def test_newif_and_includeonly(self):
        result = self.scan(r"\newif\ifdraft\ifdraft\cite{old}\fi\drafttrue"
            r"\ifdraft\cite{live}\fi\includeonly{one}\include{one}\include{two}",
            {"one.tex": r"\cite{included}", "two.tex": r"\cite{excluded}"})
        self.assertEqual([c.keys for c in result.citations], [["live"], ["included"]])

    def test_nested_input_paths_resolve_from_compilation_directory(self):
        result = self.scan(r"\input{sub/child}",
            {"sub/child.tex": r"\input{next}", "next.tex": r"\cite{root_relative}",
             "sub/next.tex": r"\cite{wrong_directory}"})
        self.assertEqual([c.keys for c in result.citations], [["root_relative"]])

    def test_verbatim_and_inert_definitions(self):
        result = self.scan(r"""\newcommand{\foo}{ordinary text}
\verb|% \cite{example}| \citep{live}
\begin{verbatim}
% \cite{example2} \iffalse
\end{verbatim}
\begin{comment}\cite{example3}\end{comment}
""")
        self.assertEqual([c.keys for c in result.citations], [["live"]])

    def test_unsupported_constructs_fail_instead_of_guessing(self):
        for text in (r"\ifnum1=1\cite{a}\fi", r"\input{\chapterfile}",
                     r"\newcommand{\mycite}{\citep{a}}\mycite", r"\iffalse\cite{a}"):
            with self.subTest(text=text), self.assertRaises(ScanError):
                self.scan(text)

    def test_compiled_aux_recursion_and_bbl_optional_label(self):
        with fixture_directory() as directory:
            root = Path(directory)
            (root / "manuscript.aux").write_text(r"\citation{a,b}\@input{child.aux}", encoding="utf-8")
            (root / "child.aux").write_text(r"\citation{c}", encoding="utf-8")
            (root / "manuscript.bbl").write_text(r"\bibitem[{A [{nested}](2024)}]{a}\bibitem{b}\bibitem{c}", encoding="utf-8")
            result = compiled_keys(root)
            self.assertEqual(result["aux_commands"], [["a", "b"], ["c"]])
            self.assertEqual(result["bbl_keys"], ["a", "b", "c"])

    def test_escaped_percent_does_not_hide_later_comment(self):
        value = strip_comments("x \\% visible % hidden\nnext")
        self.assertIn("visible", value)
        self.assertNotIn("hidden", value)
        self.assertEqual(len(value), len("x \\% visible % hidden\nnext"))

    def test_equation_does_not_turn_preceding_prose_into_table_row(self):
        result = self.scan(r"""First sentence. A supported claim \cite{a} is here.
\begin{equation}\begin{aligned}x & = y \\\end{aligned}\end{equation}""")
        self.assertEqual(result.citations[0].kind, "prose")
        self.assertEqual(result.citations[0].original_sentence, r"A supported claim \cite{a} is here.")


if __name__ == "__main__":
    unittest.main()
