#read invited names list
name_list = []
with open(r"Mail Merge Project\mail_Input\Names\invited_names.txt") as name_file:
    while True:
        line = name_file.readline()
        if not line:
            break
        if line != "\n":
            name_list.append(line.strip())
#read letter 
with open(r"Mail Merge Project\mail_Input\Letters\starting_letter.txt") as letter_file:
    letter_list = letter_file.readlines()
#create function to write new letters 
def write_letter(name):
    letter = letter_list.copy()
    letter[0] = letter[0].replace('[Name]',name)
    print(letter)
    new_letter_path = r"Mail Merge Project\mail_Output\ReadyToSend\letter_for_{0}".format(name)
    with open(new_letter_path,"w") as new_letter:
        for line in letter:
            new_letter.write(line)

for name in name_list:
    write_letter(name)
print(name_list)
