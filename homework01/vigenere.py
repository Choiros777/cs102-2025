def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    arr = []
    alphabet = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    newshiftarr = []
    newshift = 0

    if len(plaintext) > len(keyword):
        for i in range(len(plaintext) // len(keyword)):
            newkeyword = keyword + keyword[0 : len(plaintext) - len(keyword)]
            keyword = newkeyword

    for char in keyword:
        if char.isupper() == True:
            newshift = ord(char) - 65
        if char.islower() == True:
            newshift = ord(char) - 97

        newshiftarr.append(newshift)

    i = 0

    for char in plaintext:
        if char.isupper() == True:
            if (90 - ord(char)) < newshiftarr[i]:
                if newshiftarr[i] > 26:
                    a = newshiftarr[i] - newshiftarr[i] % 26
                a = abs(90 - (ord(char) + newshiftarr[i]))
                arr.append(chr(65 + a - 1))
                i = i + 1
            else:
                arr.append(chr(ord(char) + newshiftarr[i]))
                i = i + 1

        elif char.islower() == True:
            if (122 - ord(char)) < newshiftarr[i]:
                if newshiftarr[i] > 26:
                    a = newshiftarr[i] - newshiftarr[i] % 26
                a = abs(122 - (ord(char) + newshiftarr[i]))
                arr.append(chr(97 + a - 1))
                i = i + 1
            else:
                arr.append(chr(ord(char) + newshiftarr[i]))
                i = i + 1

        else:
            arr.append(char)
            i += 1

    ciphertext = "".join(arr)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    newshiftarr = []
    newshift = 0

    if len(ciphertext) > len(keyword):
        for i in range(len(ciphertext) // len(keyword)):
            newkeyword = keyword + keyword[0 : len(ciphertext) - len(keyword)]
            keyword = newkeyword

    for char in keyword:
        if char.isupper() == True:
            newshift = ord(char) - 65
        if char.islower() == True:
            newshift = ord(char) - 97

        newshiftarr.append(newshift)

    arr = []
    i = 0
    for char in ciphertext:
        if 65 <= ord(char) <= 90:
            if abs(65 - ord(char)) < newshiftarr[i]:
                if newshiftarr[i] > 26:
                    a = newshiftarr[i] - newshiftarr[i] % 26
                a = abs(65 - (ord(char) - newshiftarr[i]))
                arr.append(chr(90 - a + 1))
                i = i + 1
            else:
                arr.append(chr(ord(char) - newshiftarr[i]))
                i = i + 1

        elif 97 <= ord(char) <= 122:
            if abs(97 - ord(char)) < newshiftarr[i]:
                if newshiftarr[i] > 26:
                    a = newshiftarr[i] - newshiftarr[i] % 26
                a = abs(97 - (ord(char) - newshiftarr[i]))
                arr.append(chr(122 - a + 1))
                i = i + 1
            else:
                arr.append(chr(ord(char) - newshiftarr[i]))
                i = i + 1
        else:
            arr.append(char)
            i = i + 1
    plaintext = "".join(arr)
    return plaintext
