import pandas
data = pandas.read_csv(r"NATO alphabet\nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter : row.code for (index,row) in data.iterrows()}
word = input("Enter Word : ")
output_list = [phonetic_dict[letter] for letter in word.upper()]
print(output_list)
