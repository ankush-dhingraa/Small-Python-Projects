from logo import logo
print(logo)
print("*******************************[ START ]******************************")
#creating a functions for calculation 
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

calculation_over = False
previous_result = False
while not calculation_over:
    if not previous_result:
        first = float(input("What's the first number?"))
    else:
        first = result
    # print('+\n-\n*\n/\n')
    for operator in operations:
        print(operator)
    print("\n\n")
    operator = input("Pick an operation: ")
    second = float(input("What's the next number?"))
    result = operations[operator](first,second)
    print(f"{first} {operator} {second} = {result}")
    choice = input(f"Type 'y' to continue calculating with {result},\n or type 'n' to start a new calculation or 'exit' to exit: ").lower()
    if choice == "y":
        previous_result = True
    elif choice == "n":
        print("\n"*50)
    elif choice == "exit":
        print("Good bye! :)")
        print("*******************************[ EXIT ]******************************")
        calculation_over = True
    else:
        print("Wrong choice.....starting a new calculation")
        print("\n"*50)