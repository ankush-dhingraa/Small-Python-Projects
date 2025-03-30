from money import ruppe_structure,ruppe_dict
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
    "water" : 190,
    "milk" : 450,
    "coffee" : 10,
    "money" : 0
}
#disply_menu() for display the menu to user
def display_menu():
    for keys in MENU:
        print(keys, " : ₹",MENU[keys]["cost"])

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
    global resource
    money_collect = False
    total_money = 0
    print(ruppe_structure)
    while not money_collect:
        user_input = int(input("Enter money coins or notes : "))
        total_money += ruppe_dict[user_input]
        if item_cost > total_money:
            print(f"₹{total_money} out of ₹{item_cost}, ₹{item_cost-total_money} is still pending Enter more Ruppe :(")
        elif item_cost < total_money:
            print(f"₹{total_money-item_cost} is refunded to you, Money collected :)")
            money_collect = True
        elif item_cost == total_money:
            print("Money Collected :-)")
            money_collect = True
    if money_collect == True:
        resource["money"] += total_money



check_resources("Kumbakonam Degree Coffee")


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
# display_menu()
buy_coffee = True
while buy_coffee:
    pass


        

