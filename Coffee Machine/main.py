MENU = {
    "Indian Espresso" : {"ingredients" : {
        "Water" : 50,
        "milk" : 0,
        "coffee" : 30,
    },
    "cost" : 60},
    "Kumbakonam Degree Coffee" : {"ingredients" : {
        "Water" : 120,
        "milk" : 80,
        "coffee" : 50,
    },
    "cost" : 100},
    "Hyderabadi Irani Coffee" : {"ingredients" : {
        "Water" : 80,
        "milk" : 100,
        "coffee" : 40,
    },
    "cost" : 90}
}
print(MENU["Indian Espresso"]["ingredients"])

for keys in MENU:
    print(keys," : ")
    for i in MENU[keys]:
        if i == "ingredients":
            for j in MENU[keys][i]:
                print(j," : ",MENU[keys][i][j])
        else:
            print(i," : ",MENU[keys][i])
    print("\n")
        

