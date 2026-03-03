import string
import random

def generate_password(length: int = 10):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(alphabet) for extent in range(length))
    return password

def generate_password(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for extent in range(length))

def check_password_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digits = any(c.isdigit() for c in password)
    has_symbols = any(c in "$%&*!@^" for c in password)
    
    score = sum([has_upper, has_lower, has_digits, has_symbols])

    if len(password) < 8 or score <= 1:
        return "Mahina 🔴"
    elif score <= 3:
        return "sakto lang 🟡"
    else:
        return "Maangas 🟢"
