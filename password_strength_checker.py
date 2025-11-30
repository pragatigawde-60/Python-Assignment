import re #regular expression

def chk_pswd_strgth(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True


if __name__ == "__main__":
    user_password = input("Enter your password to check its strength: ")

    if chk_pswd_strgth(user_password):
        print("✅ Strong password! Your password meets all security requirements.")
    else:
        print("❌ Weak password! Please make sure it:")
        print(" - Is at least 8 characters long")
        print(" - Contains both uppercase and lowercase letters")
        print(" - Includes at least one number (0-9)")
        print(" - Includes at least one special character (e.g., !, @, #, $, %)")
