import re

def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    score = 0
    feedback = []

    # Criteria 1: Length
    if length >= 12:
        score += 1
    elif length >= 8:
        feedback.append("Consider using a longer password for better security.")

    # Criteria 2: Presence of uppercase and lowercase letters
    if has_upper and has_lower:
        score += 1
    else:
        feedback.append("Mixing uppercase and lowercase letters enhances security.")

    # Criteria 3: Presence of numbers
    if has_digit:
        score += 1
    else:
        feedback.append("Including numbers adds to the complexity of the password.")

    # Criteria 4: Presence of special characters
    if has_special:
        score += 1
    else:
        feedback.append("Special characters provide an extra layer of security.")

    # Determine the strength of the password
    if score == 4:
        return "Strong", "Strong password! Keep it safe."
    elif score == 3:
        return "Medium", "Medium password. You can improve it by using a longer password or adding more complex characters."
    else:
        return "Weak", "Weak password. " + " ".join(feedback)


if __name__ == "__main__":
    print("Welcome to the Password Strength Checker!")
    print("Please enter your password below:")
    
    while True:
        password = input("> ")
        if password.lower() == 'exit':
            print("Exiting...")
            break
        
        strength, feedback = check_password_strength(password)
        print(feedback)

        # End the loop if the password is strong
        if strength == "Strong":
            print("Password is strong. Exiting...")
            break
        else:
            print("Please try again.")
