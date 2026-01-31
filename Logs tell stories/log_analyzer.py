# Logs Tell Stories
# Detects suspicious login behavior from logs

failed_attempts = {}

def analyze_logs(file_path):
    print("🔍 Analyzing logs...\n")

    with open(file_path, "r") as file:
        for line in file:
            if "Failed password" in line:
                ip = line.split("from")[-1].strip()
                failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

            if "Accepted password" in line:
                ip = line.split("from")[-1].strip()
                print(f"⚠️ Successful login after failures detected from IP: {ip}")

    print("\n📊 Failed Login Summary:")
    for ip, count in failed_attempts.items():
        print(f"- {ip}: {count} failed attempts")

    print("\n📌 Security Insight:")
    print("Multiple failed logins followed by success may indicate a brute-force attack.")

if __name__ == "__main__":
    analyze_logs("auth.log")