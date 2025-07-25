def caesar_cipher(message, shift, mode='encode'):
    result = ''
    shift = shift % 26
    if mode == 'decode':
        shift = -shift

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


encoded = caesar_cipher("Karthik", 3, "encode")
print(encoded)
decoded = caesar_cipher(encoded, 3, "decode")
print(decoded)
