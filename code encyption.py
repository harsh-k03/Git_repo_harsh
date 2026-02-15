import string
letter=list(string.ascii_lowercase)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

def encrypt(original_code, shift_spaces):
    encrypted_code=""
    for alph in original_code:
        if alph in letter:
            updated_position = (letter.index(alph) + shift_spaces) % len(letter)
            encrypted_code += letter[updated_position]
        else:
            encrypted_code+=alph 
    print(f"The encrypted text is : {encrypted_code}")   

def decrypt(original_code, shift_spaces):
    decrypted_code=""
    for alph in original_code:
        if alph in letter:
            updated_position = (letter.index(alph) - shift_spaces)%len(letter)
            decrypted_code += letter[updated_position]
        else:
            decrypted_code+=alph
    print(f"The decrypted code is : {decrypted_code}")


if direction=="encode" or direction=="decode":
    code = input("Type your message\n").lower()
    shift = int(input("Type the number of spaces you want to shift your letters to :\n"))
    if direction=="encode":
        encrypt(code, shift)
    elif direction=="decode":
        decrypt(code, shift)
else:
    print("Enter a valid choice!")        
        
    


# encrypt(original_code = text, shift_spaces = shift)



    
    
    




    


