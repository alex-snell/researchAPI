#!/usr/bin/env python3
import subprocess

BASE_URL = "http://localhost:5000"
EXPORT_EVERY = 5  # export after every N runs


def run(cmd: list[str]) -> None:
    """Run a command, print it, and stream output."""
    print(f"\n$ {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="")


def main():
    # Ask which condition to run
    while True:
        condition = input("Which condition to run? (A or B): ").strip().upper()
        if condition in ("A", "B"):
            break
        print("Please enter A or B.")

    endpoint = f"/con{condition}"

    # Ask how many times to loop
    while True:
        try:
            total = int(input(f"How many times should /con{condition} run? "))
            if total > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")

    export_count = 0

    for i in range(1, total + 1):
        print(f"\n=== Iteration {i}/{total} ===")

        run(["curl", f"{BASE_URL}{endpoint}"])

        if i % EXPORT_EVERY == 0 or i == total:
            print(f"\n--- Exporting → results_{export_count}.csv ---")
            run(["curl", f"{BASE_URL}/export", "--output", f"results_{export_count}_3_29.csv"])
            export_count += 1

    print(f"\nDone. {total} /con{condition} runs, {export_count} CSV(s) exported.")

    print("\n--- Final results ---")
    run(["curl", f"{BASE_URL}/results"])


if __name__ == "__main__":
    main()