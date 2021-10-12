import string
import random
import pyperclip as pc
print("-"*25, "Welcome to Random Password Generator", "-"*25)
def Generate_Password(num):
    password = ''
    print("Password Copied to clipboard")
    for n in range(num):
        x = random.randint(0, 94)
        password += string.printable[x] 

        pc.copy(password)
    return password 
n = int(input("Enter the number:"))
print(Generate_Password(n))