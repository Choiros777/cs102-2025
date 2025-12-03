def encrypt_atbash(plaintext):
    ciphertext = ""
    for char in plaintext:
        if char.isupper():
            if ord(char) < 77:
                ciphertext += chr(77 + (78 - ord(char)))
            if ord(char) > 77:
                ciphertext += chr(77 - (ord(char) - 78))
            if ord(char) == 77:
                ciphertext += "N"
        elif char.islower():
            if ord(char) < 109:
                ciphertext += chr(109 + (110 - ord(char)))
            if ord(char) > 109:
                ciphertext += chr(109 - (ord(char) - 110))
            if ord(char) == 109:
                ciphertext += "n"
        else:
            ciphertext += char
    return ciphertext


print(encrypt_atbash("AAAAAAZZZZMqecui*(*&^%$aaaaaaaaaaa"))
