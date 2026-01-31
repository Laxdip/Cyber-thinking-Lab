# Security Checklist Generator
# Generates simple security checklists for different users

def home_user_checklist():
    return [
        "Enable automatic updates on all devices",
        "Use a strong Wi-Fi password",
        "Change default router credentials",
        "Install antivirus software",
        "Backup important files regularly"
    ]

def student_checklist():
    return [
        "Lock your laptop when not in use",
        "Avoid public Wi-Fi without VPN",
        "Use unique passwords for each account",
        "Enable two-factor authentication",
        "Be careful with email attachments"
    ]

def small_business_checklist():
    return [
        "Limit admin access to necessary users",
        "Regularly update systems and software",
        "Use firewall and antivirus solutions",
        "Backup business data daily",
        "Monitor login activity"
    ]

def main():
    print("🔐 Security Checklist Generator")
    print("1. Home User")
    print("2. Student")
    print("3. Small Business")

    choice = input("Choose your profile (1/2/3): ")

    if choice == "1":
        checklist = home_user_checklist()
    elif choice == "2":
        checklist = student_checklist()
    elif choice == "3":
        checklist = small_business_checklist()
    else:
        print("Invalid choice")
        return

    print("\n🛡 Your Security Checklist:")
    for item in checklist:
        print(f"✔ {item}")

if __name__ == "__main__":
    main()
