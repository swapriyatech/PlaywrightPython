from __future__ import annotations

import argparse
import subprocess
import sys
import time


def main() -> int:
    parser = argparse.ArgumentParser(description="Benchmark pytest worker counts")
    parser.add_argument("--workers", nargs="+", type=int, default=[1, 4, 10])
    parser.add_argument("--tests", default="tests/unit tests/architecture")
    args = parser.parse_args()
    for workers in args.workers:
        started = time.perf_counter()
        command = [sys.executable, "-m", "pytest", "-n", str(workers), *args.tests.split()]
        result = subprocess.run(command, check=False, shell=False)  # noqa: S603
        elapsed = time.perf_counter() - started
        print(f"workers={workers} duration_seconds={elapsed:.2f} exit_code={result.returncode}")
        if result.returncode:
            return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
