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

resource = {
    "water" : 800,
    "milk" : 450,
    "coffee" : 185,
    "money" : 0
}
#report function for display the resources and money
def report():
    print("#"*23)
    print("current resource values".title())
    print("#"*23,"\n")
    for keys in resource:
        if keys == "money":
            print(keys," : ₹",resource[keys])
        else:
            print(keys," : ",resource[keys])
def check_resources(menu_item):
    available = True
    not_available_list = []
    for keys in MENU:
        if menu_item == keys:
            for i in MENU[keys]:
                if i == "ingredients":
                    for j in MENU[keys][i]:
                        if MENU[keys][i][j] > resource[j]:
                            available = False
                            not_available_list.append(j)
    if not available:
        print("Sorry there is not enough ",end="")
        for i in not_available_list:
            print(",",not_available_list[i])
    return available



check_resources("Hyderabadi Irani Coffee")


# print(MENU["Indian Espresso"]["ingredients"])

# for keys in MENU:
#     print(keys," : ")
#     for i in MENU[keys]:
#         if i == "ingredients":
#             for j in MENU[keys][i]:
#                 print(j," : ",MENU[keys][i][j])
#         else:
#             print(i," : ",MENU[keys][i])
#     print("\n")
        

