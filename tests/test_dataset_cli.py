"""The data verification entry point must work before any inputs are downloaded."""
from pathlib import Path
import subprocess
import sys


def test_dataset_verification_help_without_local_inputs():
    root = Path(__file__).resolve().parents[1]
    script = root / "scripts/data_prep/verify_rtx4070_final_merged_dataset.py"
    result = subprocess.run(
        [sys.executable, str(script), "--help"],
        cwd=root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=30,
    )
    assert result.returncode == 0, result.stderr
    assert "--dataset-root" in result.stdout
