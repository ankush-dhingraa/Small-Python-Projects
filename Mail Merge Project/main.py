#read invited names list
name_list = []
with open(r"Mail Merge Project\mail_Input\Names\invited_names.txt") as name_file:
    name = name_file.readline()
    name_list.append(name)

print(name_list)