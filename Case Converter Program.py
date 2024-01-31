def convert_to_snake_case(pascal_or_camel_cased_string):
    """
    Converts a string from PascalCase or camelCase to snake_case.

    Parameters:
        pascal_or_camel_cased_string (str): The input string in PascalCase or camelCase.

    Returns:
        str: The string converted to snake_case.
    """
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    """
    Main function to demonstrate the conversion of PascalCase or camelCase to snake_case.
    """
    print(convert_to_snake_case('aLongAndComplexString'))

if __name__ == '__main__':
    main()
