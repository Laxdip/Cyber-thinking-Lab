# Fake Login Page Detector
# Detects common phishing indicators in login pages

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def analyze_login_page(url):
    print("\n🔍 Analyzing:", url)

    if not url.startswith("https://"):
        print("❌ HTTPS not enabled")

    try:
        response = requests.get(url, timeout=10)
    except Exception as e:
        print("Error accessing site:", e)
        return

    soup = BeautifulSoup(response.text, "html.parser")
    forms = soup.find_all("form")

    if not forms:
        print("⚠️ No login form detected")
        return

    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    for form in forms:
        action = form.get("action")
        if action:
            if domain not in action:
                print("❌ Form submits data to external domain:", action)

    suspicious_words = ["login", "verify", "secure", "account", "password"]
    for word in suspicious_words:
        if word in response.text.lower():
            print(f"⚠️ Suspicious keyword found: '{word}'")

    print("\n✅ Analysis completed")

if __name__ == "__main__":
    target_url = input("Enter website URL to analyze: ")
    analyze_login_page(target_url)
