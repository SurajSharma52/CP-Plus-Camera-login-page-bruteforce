import subprocess
import time

def ping_with_conditions(max_successes=3, max_failures=120):
    consecutive_successes = 0
    consecutive_failures = 0
    print(f"Pinging google.com. Stops after {max_successes} successes or {max_failures} failures. Press Ctrl+C to stop.")
    try:
        while True:
            response = subprocess.run(
                ["ping", "-n", "1", "google.com"] if subprocess.os.name == "nt" else ["ping", "-c", "1", "google.com"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            if response.returncode == 0:
                print("Ping successful.")
                consecutive_successes += 1
                consecutive_failures = 0
            else:
                print("Ping failed.")
                consecutive_failures += 1
                consecutive_successes = 0

            if consecutive_successes >= max_successes:
                print(f"Ping successful {max_successes} times consecutively. Stopping.")
                break

            if consecutive_failures >= max_failures:
                print(f"Ping failed {max_failures} times consecutively. Stopping.")
                break

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nPing stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    ping_with_conditions()
