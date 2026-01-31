import re

def check_password_strength(password):
    issues = []

    if len(password) < 8:
        issues.append("Password is too short (minimum 8 characters)")

    if not re.search(r"[A-Z]", password):
        issues.append("No uppercase letter found")

    if not re.search(r"[a-z]", password):
        issues.append("No lowercase letter found")

    if not re.search(r"[0-9]", password):
        issues.append("No number found")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        issues.append("No special character found")

    if issues:
        print("\nPassword Strength: WEAK ❌")
        print("Reasons:")
        for issue in issues:
            print(f"- {issue}")
        print("\nSuggestion:")
        print("Use a longer password with mixed characters.")
    else:
        print("\nPassword Strength: STRONG ✅")
        print("Good job! Your password is hard to guess.")

if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    check_password_strength(user_password)