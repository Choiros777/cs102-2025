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

    newshiftarr = []
    newshift = 0

    ordbiga = 65
    ordsmalla = 97
    alphlen = 26


    if len(plaintext) > len(keyword):
        multiplier = (len(plaintext) + len(keyword) - 1) // len(keyword)
        keyword = keyword * multiplier

    for char in keyword:
        if char.isupper() == True:
            newshift = ord(char) - ordbiga
        if char.islower() == True:
            newshift = ord(char) - ordsmalla

        newshiftarr.append(newshift)

    i = 0

    for char in plaintext:
        if char.isupper() == True:
            if (90 - ord(char)) < newshiftarr[i]:
                if newshiftarr[i] > alphlen:
                    a = newshiftarr[i] - newshiftarr[i] % alphlen
                a = abs(90 - (ord(char) + newshiftarr[i]))
                arr.append(chr(ordbiga + a - 1))

            else:
                arr.append(chr(ord(char) + newshiftarr[i]))


        elif char.islower() == True:
            if (122 - ord(char)) < newshiftarr[i]:
                if newshiftarr[i] > alphlen:
                    a = newshiftarr[i] - newshiftarr[i] % alphlen
                a = abs(122 - (ord(char) + newshiftarr[i]))
                arr.append(chr(ordsmalla + a - 1))

            else:
                arr.append(chr(ord(char) + newshiftarr[i]))


        else:
            arr.append(char)
        i += 1

    ciphertext = "".join(arr)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:

    ordbiga = 65
    ordsmalla = 97
    alphlen = 26


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
        if char.isupper():
            newshift = ord(char) - ordbiga
        if char.islower():
            newshift = ord(char) - ordsmalla

        newshiftarr.append(newshift)

    arr = []
    indchar = 0
    for char in ciphertext:
        if ordbiga <= ord(char) <= 90:
            if abs(ordbiga - ord(char)) < newshiftarr[indchar]:
                if newshiftarr[indchar] > alphlen:
                    a = newshiftarr[indchar] - newshiftarr[indchar] % alphlen
                a = abs(ordbiga - (ord(char) - newshiftarr[indchar]))
                arr.append(chr(90 - a + 1))

            else:
                arr.append(chr(ord(char) - newshiftarr[indchar]))

        elif ordbiga <= ord(char) <= 122:
            if abs(ordsmalla - ord(char)) < newshiftarr[indchar]:
                if newshiftarr[indchar] > alphlen:
                    a = newshiftarr[indchar] - newshiftarr[indchar] % alphlen
                a = abs(ordsmalla - (ord(char) - newshiftarr[indchar]))
                arr.append(chr(122 - a + 1))

            else:
                arr.append(chr(ord(char) - newshiftarr[indchar]))

        else:
            arr.append(char)
        indchar = indchar + 1


    plaintext = "".join(arr)
    return plaintext
