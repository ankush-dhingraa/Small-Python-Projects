from logo import logo
print(logo)
print("***********************[ START ]***********************")
program_over = False
auction_bid = dict()

while not program_over:
    name = input("Please enter your name: ")
    amount = int(input("Enter your bid amount : ₹"))
    auction_bid[name] = amount
    
