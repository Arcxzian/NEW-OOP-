import string
import random
import time
import sys


def generate_password(length: int = 16): 
    alphabet = string.ascii_letters + string.digits + string.punctuation 
    return "".join(random.choice(alphabet) for extent in range(length))

def check_password_strength(password): 
    has_upper = any(letter.isupper() for letter in password)    
    has_lower = any(letter.islower() for letter in password)
    has_digits = any(digit.isdigit() for digit in password)
    has_symbols = any(mark in string.punctuation for mark in password)
    
    score = sum([has_upper, has_lower, has_digits, has_symbols]) 

    if len(password) < 10 or score <= 2:
        return "Mahina 🔴"
    elif score <= 3:
        return "sakto lang 🟡"
    else:
        return "Maangas 🟢"

def get_user_input(prompt, min_val=6, max_val=16): 
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
def spacer():
    print("\n" + "-"*40 + "\n")
            
def generate_password_flow(): 
    while True:
        length = get_user_input("Specify The Length of Your Password (6-16): ")
        password =  generate_password(length)
        strength = check_password_strength(password)        
        
        print(f"\nGenerated Password: {password}")
        print(f"Strength: {strength}")
        
        if strength != "Maangas 🟢": 
            print("Password is not strong enough. Generating again...\n")
            time.sleep(1)
            continue

        retry = input("Keep this password? (yes/no): ").lower()
        if retry == "yes":
            return password
        
def countdown_exit(): 
    for extent in range(3, 0 ,-1):
        spacer()
        print(f"Existing Program in {extent} seconds...")
        time.sleep(1)
    sys.exit()
    
def main():
    print("Password Generator and Strength Checker")
    generate_password_flow()
    countdown_exit()
    
if __name__ == "__main__":
    main()
