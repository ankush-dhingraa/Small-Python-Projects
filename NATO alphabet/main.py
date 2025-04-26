import pandas
data = pandas.read_csv(r"NATO alphabet\nato_phonetic_alphabet.csv")
data_dict = {row.letter : row.code for (index,row) in data.iterrows()}
# print(data)
# print(data_dict)
NATO = []
user_input = input("Enter Word : ")
for i in user_input.upper().split():
    for key,value in data_dict.items():
        if i == key:
            NATO.append(value)

print(NATO)
