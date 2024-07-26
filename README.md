# Password Complexity Checker

A tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. Provide feedback to users on the password's strength.

# How It Works
The script uses regular expressions to check for the following criteria:

- **Length Check**: The password must be at least 8 characters long.
- **Uppercase Letter Check**: The password must contain at least one uppercase letter.
- **Lowercase Letter Check**: The password must contain at least one lowercase letter.
- **Number Check**: The password must contain at least one numeric character.
- **Special Character Check**: The password must contain at least one special character.

Based on these checks, the script assigns a strength score to the password. A password with a score of 5 is considered "Strong", a score between 3 and 4 is "Moderate", and a score less than 3 is "Weak".
