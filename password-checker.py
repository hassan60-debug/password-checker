import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Use 12+ characters for better security")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Add uppercase letters (A-Z)")

    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Add lowercase letters (a-z)")

    # Number check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        suggestions.append("Add numbers (0-9)")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        suggestions.append("Add special characters (!@#$%^&*)")

    # Common passwords check
    common = ["password", "123456", "qwerty", "abc123", "password123"]
    if password.lower() in common:
        score = 0
        suggestions = ["This is a very common password — change it immediately!"]

    # Result
    print(f"\n{'='*45}")
    print(f"  Password Strength Checker")
    print(f"{'='*45}")
    print(f"  Password : {'*' * len(password)}")
    print(f"  Score    : {score}/6")

    if score <= 2:
        print(f"  Strength : ❌ WEAK")
    elif score <= 4:
        print(f"  Strength : ⚠️  MEDIUM")
    else:
        print(f"  Strength : ✅ STRONG")

    if suggestions:
        print(f"\n  Suggestions:")
        for s in suggestions:
            print(f"   → {s}")

    print(f"{'='*45}\n")

# Run
while True:
    pwd = input("Enter password to check (or 'quit' to exit): ")
    if pwd.lower() == 'quit':
        break
    check_password_strength(pwd)