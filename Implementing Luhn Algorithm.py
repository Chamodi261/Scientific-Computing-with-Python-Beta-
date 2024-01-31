def verify_card_number(card_number):
    """
    Verifies the validity of a credit card number using the Luhn algorithm.

    Parameters:
        card_number (str): The credit card number to be verified.

    Returns:
        bool: True if the credit card number is valid, False otherwise.
    """
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    # Calculate the sum of odd digits
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]

    # Calculate the sum of even digits after doubling
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    """
    Main function to demonstrate credit card number validation.
    """
    card_number = '4111-1111-4555-1141'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

# Run the main function
main()
