"""Coolest art entry: copy the vendored artwork byte-identically to /output/entry.png.

Stdlib only, no network, deterministic: the output is an exact byte copy of
art.png shipped in this repo.
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    src = HERE / "art.png"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
