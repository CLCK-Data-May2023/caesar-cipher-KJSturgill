# add your code here
plaintext= input("Enter sentence to encrypt:").lower()
encryptedtext = ""
for i in range(len(plaintext)):
        letter = plaintext[i]

        if ord(letter) < 97 or ord(letter) > 122:
            encryptedtext+=letter

        else:
            encryptedtext += chr((ord(letter) + 5-97) % 26 + 97)

print("The encrypted sentence is: " + encryptedtext)  