import logo
print(logo.logo)
print("***************************[START]****************************")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(original_text,shift):
    encrypted_text = ""
    for letters in original_text:
        if letters == " ":
            encrypted_text += " "
        else:
            encrypted_text += alphabet[(alphabet.index(letters)-len(alphabet))+shift]
    print(f"Encrypted text is : {encrypted_text}\n")

def decrypt(original_text,shift):
    decryted_text = ""
    for letter in original_text:
        if letter == " ":
            decryted_text += " "
        else:
            decryted_text += alphabet[alphabet.index(letter)-shift]
    print(f"Decrypted text is : {decryted_text}\n")
def caesar(original_text, shift, encode_or_decode):
    if encode_or_decode.lower() == "encode":
        encrypt(original_text,shift)
    elif encode_or_decode.lower() == "decode":
        decrypt(original_text,shift)
    else:
        print("Wrong choice, do agian")

stop = False
while not stop:
    encode_or_decode = input("Enter 'encode' to encrypt or 'decode' to decrypt : ")
    text = input(f"Enter the text to {encode_or_decode} : ").lower()
    shift = int(input("Enter the shift value : "))
    caesar(text,shift,encode_or_decode)
    choice = input("Enter 'yes' to try again, or 'no' to exit : ").lower()
    if choice == "yes":
        stop = False
    elif choice == "no":
        stop = True
        print("***************************[EXIT]****************************")
