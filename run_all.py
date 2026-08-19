# Run All Scripts
# This file runs all 4 steps of the project one after another

import subprocess
import sys

scripts = [
    "01_data_loading_and_cleaning.py",
    "02_analysis.py",
    "03_visualizations.py",
    "04_inferences.py"
]

for script in scripts:
    print(f"\n{'='*50}")
    print(f"  Running: {script}")
    print(f"{'='*50}\n")
    result = subprocess.run([sys.executable, script])
    if result.returncode != 0:
        print(f"\nError running {script}! Stopping.")
        break

print("\n\nAll done!")
