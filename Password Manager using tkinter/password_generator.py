import random
#Lists of letters, numbers and symbols to be used in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Hello! Welcome to the Python Password Generator!")
# nr_letters = int(input("Enter the number of letters you want in your password:\n"))
# nr_symbols = int(input("How many special characters would you like to include?\n"))
# nr_numbers = int(input("Specify the number of digits you need:\n"))

#Generating the password by randomly selecting characters from the lists
def create_password():
    list_password = []
    for i in range(1,5):
        list_password.append(random.choice(letters))
    for i in range(1,5):
        list_password.append(random.choice(numbers))
    for i in range(1,5):
        list_password.append(random.choice(symbols))

    #Shuffling the password
    random.shuffle(list_password)
    password = ""
    for char in list_password:
        password += char
    return password
