import re

def password_strength_checker(password):
    # Criteria definitions
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None

    # Initialize strength score
    strength_score = 0

    # Evaluate criteria
    if length_criteria:
        strength_score += 1
    if uppercase_criteria:
        strength_score += 1
    if lowercase_criteria:
        strength_score += 1
    if number_criteria:
        strength_score += 1
    if special_criteria:
        strength_score += 1

    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_criteria:
        feedback.append("Password should include at least one special character.")

    # Determine strength level
    if strength_score == 5:
        strength_level = "Strong"
    elif 3 <= strength_score < 5:
        strength_level = "Moderate"
    else:
        strength_level = "Weak"

    return strength_level, feedback

# Example usage
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength_level, feedback = password_strength_checker(password)
    print(f"Password Strength: {strength_level}")
    if feedback:
        print("Feedback:")
        for comment in feedback:
            print(f"- {comment}")
