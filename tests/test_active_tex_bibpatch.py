"""Bibliography patch conditionals must not mask actual manuscript citations."""
from pathlib import Path
import sys,tempfile,unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from active_tex import ScanError,scan_manuscript

class BibliographyPatchScanTests(unittest.TestCase):
    def scan(self,patch):
        task_tmp=Path(__file__).resolve().parents[1]/'.cache'/'tests'/'apa7_scanner_tests'
        task_tmp.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryDirectory(dir=task_tmp) as directory:
            root=Path(directory)
            assert root.resolve().is_relative_to(task_tmp.resolve())
            (root/'manuscript.tex').write_text(patch+'\n'+r'\begin{document}\citep{realkey}\end{document}',encoding='utf-8')
            return scan_manuscript(root)

    def test_deferred_field_conditional_keeps_real_citation(self):
        result=self.scan(r'\xpatchbibmacro{addinfo1}{\printfield{pages}}{\iffieldundef{eid}{\printfield{pages}}{\printfield{eid}}}{}{\PackageError{test}{failure}{help}}')
        self.assertEqual([c.keys for c in result.citations],[['realkey']])

    def test_hidden_citation_is_rejected(self):
        with self.assertRaisesRegex(ScanError,'Dynamic citation/input'):
            self.scan(r'\xpatchbibmacro{addinfo1}{\printfield{pages}}{\citep{hidden}}{}{}')

    def test_hidden_source_input_is_rejected(self):
        with self.assertRaisesRegex(ScanError,'Dynamic citation/input'):
            self.scan(r'\xpatchbibmacro{addinfo1}{\printfield{pages}}{\input{hidden}}{}{}')

if __name__=='__main__':unittest.main()
