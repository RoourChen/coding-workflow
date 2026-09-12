import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "init_task.py"


class InitTaskTests(unittest.TestCase):
    def command(self, project: str) -> list[str]:
        return [
            sys.executable,
            str(SCRIPT),
            "--project",
            project,
            "--title",
            "Add export",
            "--goal",
            "Users can export a report.",
            "--non-goal",
            "Do not redesign the report screen.",
            "--done",
            "Export produces a valid CSV file.",
            "--verify",
            "python -m unittest",
        ]

    def test_creates_task_file(self):
        with tempfile.TemporaryDirectory() as project:
            result = subprocess.run(self.command(project), capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            content = (Path(project) / "TASK.md").read_text(encoding="utf-8")
            self.assertIn("# Task: Add export", content)
            self.assertIn("## Non-goals", content)
            self.assertIn("`python -m unittest`", content)

    def test_refuses_to_overwrite(self):
        with tempfile.TemporaryDirectory() as project:
            path = Path(project) / "TASK.md"
            path.write_text("keep me", encoding="utf-8")
            result = subprocess.run(self.command(project), capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(path.read_text(encoding="utf-8"), "keep me")

    def test_rejects_output_outside_project(self):
        with tempfile.TemporaryDirectory() as project:
            command = self.command(project) + ["--output", "../TASK.md"]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("inside the project", result.stderr)


if __name__ == "__main__":
    unittest.main()
