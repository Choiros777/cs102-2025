
def encrypt_atbash(plaintext):
    ciphertext = ''
    arr = []
    i=0
    for char in plaintext:

        if char.isupper() == True: #90-65
            charnumber = int(26 - (ord(char) - 64) + 1)
            arr.append(chr(64+charnumber))

        elif char.islower() == True: #122-97
            charnumber = int(26 - (ord(char) - 96) + 1)
            arr.append(chr(96 + charnumber))
        else:
            arr.append(char)
            i += 1

    ciphertext = "".join(arr)

    return ciphertext


print(encrypt_atbash("zzzaaa"))
print(encrypt_atbash("NOON"))
print(encrypt_atbash("Gr8"))