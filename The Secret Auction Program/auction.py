from logo import logo
print(logo)
print("***********************[ START ]***********************")
program_over = False
auction_bid = dict()

while not program_over:
    name = input("Please enter your name: ")
    amount = int(input("Enter your bid amount : ₹"))
    auction_bid[name] = amount
    choice = input("Are there any other bidders? Reply with 'yes' or 'no' : ").lower()
    if choice == "yes":
        print("\n"*50)
    elif choice == "no":
        highest_bider_name =""
        highest_bid = 0
        for key in auction_bid:
            value = auction_bid[key]
            if highest_bid < value:
                highest_bider_name = key
                highest_bid = value
        print(f"\n\nThe winner is {highest_bider_name} with a bid of ₹{highest_bid}")                
        program_over = True
        print("\n***********************[ EXIT ]***********************")
    else:
        print("\n Wrong choice :( ")
        print("\n"*50)



    
