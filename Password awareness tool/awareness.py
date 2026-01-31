# Password Awareness Tool
# This tool educates users about leaked and risky passwords

COMMON_PASSWORDS = [
    "123456", "password", "123456789", "qwerty",
    "abc123", "password123", "admin", "letmein",
    "welcome", "iloveyou"
]

def check_password_awareness(password):
    print("\n🔍 Password Awareness Report")

    if password.lower() in COMMON_PASSWORDS:
        print("❌ HIGH RISK")
        print("Reason:")
        print("- This password is commonly found in leaked databases.")
        print("- Attackers try this password first.")
    else:
        print("⚠️ MODERATE RISK")
        print("Reason:")
        print("- Password not found in common leaks.")
        print("- Still unsafe if reused elsewhere.")

    print("\n🛡 Security Advice:")
    print("- Never reuse passwords.")
    print("- Use a password manager.")
    print("- Long passphrases are safer than short complex ones.")

if __name__ == "__main__":
    user_password = input("Enter a password for awareness check: ")
    check_password_awareness(user_password)