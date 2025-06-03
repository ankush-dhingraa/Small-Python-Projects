import pandas
data = pandas.read_csv(r"NATO alphabet\nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter : row.code for (index,row) in data.iterrows()}
flag =True
while flag:
    try:
        word = input("Enter Word : ")
        output_list = [phonetic_dict[letter] for letter in word.upper()]
        print(output_list)
    except:
        print("sorry, only letters in the alphabet please.")
    else:
        flag = False

# def generate_phonetic():
#     word = input("Enter Word : ")
#     try:
#         output_list = [phonetic_dict[letter] for letter in word.upper()]
#     except KeyError:
#         print("sorry, only letters in the alphabet please.")
#         generate_phonetic()
#     else:
#         print(output_list)
# generate_phonetic()



