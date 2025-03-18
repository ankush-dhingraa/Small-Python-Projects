alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(original_text,shift):
    encrypted_text = ""
    for letters in original_text:
        if letters == " ":
            encrypted_text += " "
        else:
            encrypted_text += alphabet[(alphabet.index(letters)-len(alphabet))+shift]
    print(f"Encrypted text is : {encrypted_text}")

def decrypt(original_text,shift):
    decryted_text = ""
    for letter in original_text:
        if letter == " ":
            decryted_text += " "
        else:
            decryted_text += alphabet[alphabet.index(letter)-shift]
    print(f"Decrypted text is : {decryted_text}")

text = input("Enter the text to encrypt : ").lower()
shift = int(input("Enter the shift value : "))
encrypt(text,shift)
text = input("Enter the text to decrypt : ").lower()
shift = int(input("Enter the shift value : "))
decrypt(text,shift)