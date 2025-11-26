import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    elif re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password):
        return "Strong"
    else:
        return "Medium"

password = input("Enter password: ")
print(check_password_strength(password))
