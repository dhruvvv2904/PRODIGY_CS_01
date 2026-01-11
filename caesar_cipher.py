def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("=== Caesar Cipher Program ===")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

choice = input("Type 'e' for encryption or 'd' for decryption: ").lower()

if choice == 'e':
    encrypted_text = encrypt(message, shift)
    print("Encrypted Text:", encrypted_text)

elif choice == 'd':
    decrypted_text = decrypt(message, shift)
    print("Decrypted Text:", decrypted_text)

else:
    print("Invalid choice!")

