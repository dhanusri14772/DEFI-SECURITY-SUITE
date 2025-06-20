analyze.py

import subprocess
import json

CONTRACT_PATH = "../smart_contracts/sample.sol"  
OUTPUT_FILE = "reports/security_analysis.json"

def run_slither():
    print("[+] Running Slither analysis...")
    result = subprocess.run(
        ["slither", CONTRACT_PATH, "--json", "reports/slither.json"],
        capture_output=True,
        text=True
    )
    return json.loads(result.stdout) if result.stdout else {}

def run_mythril():
    print("[+] Running Mythril analysis...")
    result = subprocess.run(
        ["myth", "analyze", CONTRACT_PATH, "-o", "json"],
        capture_output=True,
        text=True
    )
    return json.loads(result.stdout) if result.stdout else {}

def main():
    slither_results = run_slither()
    mythril_results = run_mythril()

    
    combined_results = {
        "slither": slither_results,
        "mythril": mythril_results
    }

   
    with open(OUTPUT_FILE, "w") as f:
        json.dump(combined_results, f, indent=4)

    print(f"[✔] Security analysis saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()