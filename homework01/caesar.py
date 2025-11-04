def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    arr = []
    for char in plaintext:
        if char.isupper() == True:
            if (90 - ord(char)) < shift:
                if shift > 26:
                    a = shift - shift % 26
                a = abs(90 - (ord(char) + shift))
                arr.append(chr(65 + a - 1))
            else:
                arr.append(chr(ord(char) + shift))

        elif char.islower() == True:
            if (122 - ord(char)) < shift:
                if shift > 26:
                    a = shift - shift % 26
                a = abs(122 - (ord(char) + shift))
                arr.append(chr(97 + a - 1))
            else:
                arr.append(chr(ord(char) + shift))

        else:
            arr.append(char)
    ciphertext = "".join(arr)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    arr = []
    for char in ciphertext:
        if 65 <= ord(char) <= 90:
            if abs(65 - ord(char)) < shift:
                if shift > 26:
                    a = shift - shift % 26
                a = abs(65 - (ord(char) - shift))
                arr.append(chr(90 - a + 1))
            else:
                arr.append(chr(ord(char) - shift))

        elif 97 <= ord(char) <= 122:
            if abs(97 - ord(char)) < shift:
                if shift > 26:
                    a = shift - shift % 26
                a = abs(97 - (ord(char) - shift))
                arr.append(chr(122 - a + 1))
            else:
                arr.append(chr(ord(char) - shift))
        else:
            arr.append(char)
    plaintext = "".join(arr)
    return plaintext
