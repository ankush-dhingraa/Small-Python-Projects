from logo import logo
print(logo)
print("*******************************[ START ]*******************************")
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

calculation = False
while not calculation:
    previous
    first = float(input("What's the first number?"))
    print('+\n-\n*\n/\n')
    operator = input("Pick an operation: ")
    second = float(input("What's the next number?"))
    result = operations[operator](first,second)
    print(f"{first} {operator} {second} = {result}")
    choice = input(f"Type 'y' to continue calculating with {result},\n or type 'n' to start a new calculation or 'exit' to exit: ").lower()
    if c

