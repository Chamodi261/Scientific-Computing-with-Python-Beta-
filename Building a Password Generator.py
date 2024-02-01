import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Generate a random password that satisfies specified constraints.

    Parameters:
    - length (int): Length of the password (default is 16).
    - nums (int): Minimum number of digits in the password (default is 1).
    - special_chars (int): Minimum number of special characters in the password (default is 1).
    - uppercase (int): Minimum number of uppercase letters in the password (default is 1).
    - lowercase (int): Minimum number of lowercase letters in the password (default is 1).

    Returns:
    - str: Generated password that satisfies the specified constraints.
    """
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),  # Ensure at least 'nums' digits
            (special_chars, fr'[{symbols}]'),  # Ensure at least 'special_chars' special characters
            (uppercase, r'[A-Z]'),  # Ensure at least 'uppercase' uppercase letters
            (lowercase, r'[a-z]')  # Ensure at least 'lowercase' lowercase letters
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password
    
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)
