def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        # Проверяем, является ли символ буквой
        if char.isalpha():
            # Устанавливаем смещение для заглавных и строчных букв
            start = ord('A') if char.isupper() else ord('a')
            # Шифруем символ с учетом смещения
            encrypted_char = chr(start + (ord(char) - start + shift) % 26)
            encrypted_text += encrypted_char
        else:
            # Если символ не буква, добавляем его без изменений
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def crack_caesar_cipher(encrypted_text):
    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(encrypted_text, shift)
        print(f"Shift {shift}: {decrypted_text}")


if __name__ == "__main__":
    original_text = "Hello, World!"
    shift_value = 3

    encrypted = caesar_encrypt(original_text, shift_value)
    print(f"Encrypted: {encrypted}")

    decrypted = caesar_decrypt(encrypted, shift_value)
    print(f"Decrypted: {decrypted}")

    crack_caesar_cipher(encrypted)
