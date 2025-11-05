
def encrypt_atbash(plaintext):
    ciphertext = ""
    arr = []
    i = 0
    for char in plaintext:

        if char.isupper() == True:
            charnumber = int(26 - (ord(char) - 64) + 1)
            arr.append(chr(64 + charnumber))

        elif char.islower() == True:
            charnumber = int(26 - (ord(char) - 96) + 1)
            arr.append(chr(96 + charnumber))
        else:
            arr.append(char)
            i += 1

    ciphertext = "".join(arr)

    return ciphertext

print(encrypt_atbash("aazz"))


