import tempfile
import unittest
from pathlib import Path

from click.testing import CliRunner

import build


class LatexCommandTest(unittest.TestCase):
    def test_latex_accepts_config_and_output_paths(self):
        runner = CliRunner()
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            config_path = tmp / "config.yaml"
            output_path = tmp / "out" / "cv.tex"
            config_path.write_text(
                """
---
name: Test User
email: test@example.com
phone: "+44 0000"
location: London, UK
github: https://github.com/example
linkedin: https://linkedin.com/in/example
about_me:
  - Builds reliable systems.
core_skills:
  - Python
technology:
  languages:
    - Python
work:
  - date: 2025 - Present
    page_break_before: true
    title: Staff Engineer
    where: Example
    city: London
    description: []
    stack: []
education: []
publications: []
talks: []
interests: []
""".lstrip(),
                encoding="utf-8",
            )

            result = runner.invoke(
                build.cli,
                ["latex", "--config", str(config_path), "--output", str(output_path)],
            )

            self.assertEqual(result.exit_code, 0, result.output)
            self.assertTrue(output_path.exists())
            rendered = output_path.read_text(encoding="utf-8")
            self.assertIn(r"\cvheader{Test User}", rendered)
            self.assertIn("London, UK", rendered)
            self.assertIn(r"\newpage", rendered)
            self.assertIn("Python", rendered)


if __name__ == "__main__":
    unittest.main()
