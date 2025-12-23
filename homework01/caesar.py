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
    ordbiga = 65
    ordsmalla = 97
    alphlen = 26
    ciphertext = ""
    for char in plaintext:
        if char.isupper():
            ciphertext += chr(ordbiga + (ord(char) - ordbiga + shift) % alphlen)
        elif char.islower():
            ciphertext += chr(ordsmalla + (ord(char) - ordsmalla + shift) % alphlen)
        else:
            ciphertext += char
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
    ordbiga = 65
    ordsmalla = 97
    alphlen = 26

    for char in ciphertext:
        if char.isupper():
            plaintext += chr(ordbiga + (ord(char) - ordbiga - shift) % alphlen)
        elif char.islower():
            plaintext += chr(ordsmalla + (ord(char) - ordsmalla - shift) % alphlen)
        else:
            plaintext += char
    return plaintext
