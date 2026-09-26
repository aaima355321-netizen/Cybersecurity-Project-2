# Project 2: Basic Encryption & Decryption
# Technique: Caesar Cipher

# Function to encrypt the text
def encrypt_text(text, key):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))

        elif char.islower():
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))

        else:
            result += char

    return result


# Function to decrypt the text
def decrypt_text(text, key):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') - key) % 26 + ord('A'))

        elif char.islower():
            result += chr((ord(char) - ord('a') - key) % 26 + ord('a'))

        else:
            result += char

    return result


# Main program
print("===== Basic Encryption & Decryption =====")

text = input("Enter your text: ")
key = int(input("Enter encryption key (1-25): "))

# Encrypt the text
encrypted_text = encrypt_text(text, key)

# Decrypt the encrypted text
decrypted_text = decrypt_text(encrypted_text, key)

# Display results
print("\nOriginal Text:  ", text)
print("Encrypted Text: ", encrypted_text)
print("Decrypted Text: ", decrypted_text)