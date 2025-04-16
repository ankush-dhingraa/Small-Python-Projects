#read invited names list
name_list = []
with open(r"Mail Merge Project\mail_Input\Names\invited_names.txt") as name_file:
    while True:
        line = name_file.readline()
        if not line:
            break
        name_list.append(line.strip())

#read letter 
with open(r"Mail Merge Project\mail_Input\Letters\starting_letter.txt") as letter_file:
    letter_list = letter_file.readlines()

def write_letter(name):
    letter = letter_list.copy()
    letter[0] = letter[0].replace('[name]',name)
    print(letter)
    new_letter_path = r"Mail Merge Project\mail_Output\ReadyToSend\lettr_for_{0}".format(name)
    with open(new_letter_path,"w") as new_letter:
        for line in letter:
            new_letter.write(line)

write_letter("lavisha")
