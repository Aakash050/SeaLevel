import argparse
from pathlib import Path
import sys

def main(data_path: str = None):
    print("✅ Project scaffold is set up.")
    if data_path:
        p = Path(data_path)
        if p.exists():
            print(f"📦 Found data at: {p.resolve()}")
        else:
            print(f"⚠️ Data path not found: {p}", file=sys.stderr)
    print("🔎 Run the analysis via the Jupyter notebook at notebooks/project_notebook_clean.ipynb")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the analysis pipeline (stub).")
    parser.add_argument("--data", type=str, help="Path to a data file or folder", default=None)
    args = parser.parse_args()
    main(args.data)
