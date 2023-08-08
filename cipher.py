"""
This Ceaser cypher uses ASCII to shift characters.
It takes user input, shifts the letter a certain number over, and outputs a jumbled message to encrypt the message.
"""
#this takes user input and sets it to lowercase letters
plaintext= input("Enter sentence to encrypt:").lower()
#this adds a blank string for the program to write the encrypted message
encryptedtext = ""

for i in range(len(plaintext)):
        letter = plaintext[i]
        #this will check ifeach character in the string is a lowercase letter, all letters were made lowercase, so if it isnt a letter, its punctuation and doesnt need jumbled.
        if ord(letter) < 97 or ord(letter) > 122:
            encryptedtext+=letter

        #this line is simplified for ease of writing, but can be confusing. it takes the ord() of the letter and subtracts 97, to get a number between 1 and 26
        #the +5 is the shift, I used the number 5 instead of a variable from input because the guidelines of the assignment wont accept a second input.
        #so the parentheses determines what position in the alphabet the letter is, and adds 5. then %26 is there for the letters of the alphabet shifter past the end of the alphabet
        #if the pink parentheses is >=26, %26 will output the remainder so the end of the alphabet wraps around to the beginning. the +97 puts you back in range of the ASCII alphabet
        #finally, chr() takes all that math and converts the final number back to a letter
        else:
            encryptedtext += chr((ord(letter) -97 +5 ) % 26 +97)
            

print("The encrypted sentence is: " + encryptedtext)  