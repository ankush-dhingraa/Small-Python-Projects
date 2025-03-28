MENU = {
    "Indian Espresso" : {"ingredients" : {
        "water" : 50,
        "milk" : 0,
        "coffee" : 30,
    },
    "cost" : 60},
    "Kumbakonam Degree Coffee" : {"ingredients" : {
        "water" : 120,
        "milk" : 80,
        "coffee" : 50,
    },
    "cost" : 100},
    "Hyderabadi Irani Coffee" : {"ingredients" : {
        "water" : 80,
        "milk" : 100,
        "coffee" : 40,
    },
    "cost" : 90}
}

resource = {
    "water" : 10,
    "milk" : 450,
    "coffee" : 10,
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
#check_resources function check resource and display the ingredients if not available
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
            print(",",i,end="")
        print("\n")
    return available
#collect_money fuunction collect the money from user
def collect_money(item_cost):
    print('''
0 for ₹1 coin
1 for ₹2 coin
2 for ₹5 coin
3 for ₹10 Note
4 for ₹20 Note
5 for ₹50 Note
6 for ₹100 Note
7 for ₹200 Note
8 for ₹500 Note''')


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
        

