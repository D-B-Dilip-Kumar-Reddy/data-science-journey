# Day 1 Mini Task (Extended)
# Goal:
# 1. Safely aggregate execution results
# 2. Handle edge cases
# 3. Parse results from CSV / log-like input

import os
import csv
from collections import defaultdict

# -----------------------------
# Configuration
# -----------------------------

KNOWN_STATUSES = {"PASS", "FAIL", "CRASH"}
UNKNOWN_STATUS_KEY = "UNKNOWN"


# -----------------------------
# Core Aggregation Logic
# -----------------------------

def aggregate_results(results):
    """
    Aggregates execution results safely.

    Handles:
    - Empty input
    - Unknown status values
    """
    summary = defaultdict(int)

    if not results:
        print("WARNING: No execution data provided.")
        return summary

    for result in results:
        if result in KNOWN_STATUSES:
            summary[result] += 1
        else:
            summary[UNKNOWN_STATUS_KEY] += 1

    return summary


# -----------------------------
# CSV Parser
# -----------------------------

def parse_results_from_csv(file_path):
    """
    Parses execution results from a CSV file.

    Expected CSV format:
    iteration,status
    1,PASS
    2,FAIL
    3,CRASH
    """
    results = []

    try:
        with open(file_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            if "status" not in reader.fieldnames:
                raise ValueError("CSV missing required 'status' column")

            for row in reader:
                results.append(row["status"].strip())

    except FileNotFoundError:
        print(f"ERROR: File not found -> {file_path}")
    except Exception as e:
        print(f"ERROR while parsing CSV: {e}")

    return results


# -----------------------------
# Log Parser (Simple Example)
# -----------------------------

def parse_results_from_log(file_path):
    """
    Parses execution results from a simple log file.

    Expected log line format:
    ITERATION=10 STATUS=PASS
    """
    results = []

    try:
        with open(file_path, "r") as logfile:
            for line in logfile:
                if "STATUS=" in line:
                    status = line.split("STATUS=")[-1].strip()
                    results.append(status)

    except FileNotFoundError:
        print(f"ERROR: File not found -> {file_path}")

    return results


# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # In-memory example
    raw_results = ["PASS", "FAIL", "PASS", "CRASH", "RETRY", "UNKNOWN_STATE"]
    summary = aggregate_results(raw_results)

    print("\nExecution Summary (In-Memory Data):")
    for status, count in summary.items():
        print(f"{status}: {count}")

    # CSV example
    csv_path = os.path.join(BASE_DIR, "execution_results.csv")
    csv_results = parse_results_from_csv(csv_path)
    csv_summary = aggregate_results(csv_results)

    print("\nExecution Summary (CSV Data):")
    if not csv_summary:
        print("No valid execution data found in CSV.")
    else:
        for status, count in csv_summary.items():
            print(f"{status}: {count}")

    # Log example
    log_path = os.path.join(BASE_DIR, "execution.log")
    log_results = parse_results_from_log(log_path)
    log_summary = aggregate_results(log_results)

    print("\nExecution Summary (Log Data):")
    if not log_summary:
        print("No valid execution data found in log file.")
    else:
        for status, count in log_summary.items():
            print(f"{status}: {count}")
