"""Compatibility shim.

EIC export has been unified into chromapeak.main (CLI + YAML).
Use: python main.py --export-eic ...
"""

from chromapeak.main import main


if __name__ == "__main__":
    raise SystemExit(main())
