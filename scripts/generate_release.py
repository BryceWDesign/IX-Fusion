from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args: str) -> None:
    subprocess.run([sys.executable, *args], cwd=ROOT, check=True)


def main() -> int:
    run("scripts/run_poc.py")
    run("scripts/run_secondary_studies.py")
    run("scripts/make_manifest.py")
    print("IX-Fusion release artifacts regenerated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
