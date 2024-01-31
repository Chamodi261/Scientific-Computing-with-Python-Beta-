def vigenere(message, key, direction=1):
    """
    Encrypts or decrypts a message using the Vigenere cipher.

    Parameters:
        message (str): The message to be encrypted or decrypted.
        key (str): The key for the Vigenere cipher.
        direction (int): The direction of the operation (1 for encryption, -1 for decryption).

    Returns:
        str: The encrypted or decrypted message.
    """
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    """
    Encrypts a message using the Vigenere cipher.

    Parameters:
        message (str): The message to be encrypted.
        key (str): The key for the Vigenere cipher.

    Returns:
        str: The encrypted message.
    """
    return vigenere(message, key)
    
def decrypt(message, key):
    """
    Decrypts a message using the Vigenere cipher.

    Parameters:
        message (str): The message to be decrypted.
        key (str): The key for the Vigenere cipher.

    Returns:
        str: The decrypted message.
    """
    return vigenere(message, key, -1)

# Example usage
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'python'

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')
