import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the Password Generator")
numberOfcharacter = int(input("Please enter the number of character you want: "))
numberOfnumber = int(input("Please enter the number of numbers you want: "))
numberOfSpcharacter = int(input("Please enter the number of special character you want: "))

Selected_character = random.choices(letters, k = numberOfcharacter)
Selected_number = random.choices(numbers, k = numberOfnumber)
Selected_symbols = random.choices(symbols, k = numberOfSpcharacter)
password = Selected_character + Selected_number + Selected_symbols
random.shuffle(password)
# print(password)
newPassword = ""
for i in password:
    newPassword = i + newPassword
print("Your password could be: "+newPassword)
    