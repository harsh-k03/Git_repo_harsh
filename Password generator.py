import random
import string

letters=string.ascii_letters
numbers=string.digits
symbols=string.punctuation

print("Password Generator")
while True:
    try:
        my_let=int(input("How many letter do you want in your Password :"))
        my_num=int(input("How many numbers do you want in your password:"))
        my_sym=int(input("How many symbols do you want in your password:"))
        break
    except ValueError:
        print("Enter a valid number!")
while True:
    password = (
    random.choices(letters, k=my_let) +
    random.choices(numbers, k=my_num) +
    random.choices(symbols, k=my_sym))
    random.shuffle(password)                
  
    print("Password generated:","".join(password))
    choice=(input("Press 'R' to Regenerate Password\n")).lower()
    if choice!="r":
        break
    




