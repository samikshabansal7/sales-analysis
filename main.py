"""
main.py — Entry point for Sales Intelligence Dashboard
Run this to generate all data, charts, and Power BI exports.
"""

import subprocess, sys, os, time

def run(script, label):
    t0 = time.time()
    result = subprocess.run([sys.executable, script], capture_output=True, text=True)
    elapsed = time.time() - t0
    if result.returncode == 0:
        print(result.stdout.strip())
        print(f"   ⏱  {elapsed:.1f}s\n")
    else:
        print(f"❌ Error in {label}:\n{result.stderr}")
        sys.exit(1)

if __name__ == '__main__':
    print("=" * 60)
    print("  SALES INTELLIGENCE DASHBOARD — PIPELINE START")
    print("=" * 60 + "\n")

    # Always run from project root
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    run('src/data_generator.py', 'Data Generator')
    run('src/visualizations.py', 'Visualizations')
    run('src/ml_analytics.py',   'ML Analytics')

    print("=" * 60)
    print("  ALL OUTPUTS GENERATED")
    print("=" * 60)
    print("\n📊 Reports:         reports/")
    print("📁 Power BI Export: powerbi_exports/PowerBI_DataModel.xlsx")
    print("📂 Raw Data:        data/\n")
    print("Open reports/03_interactive_dashboard.html in your browser")
    print("for the full interactive experience!\n")
