#------Super Calculator-------#
print("Welcome to the Super Calculator!")
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
def Add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    sum = a + b
    return sum

def Subtract():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    difference = a - b
    return difference

def Multiply():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    product = a * b
    return product

def Divide():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b == 0:
        print("Error: Division by zero!")
        return None
    division = a / b
    return division

while True:
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        result = Add()
        print(f"The result of addition is: {result}")
    elif choice == "2":
        result = Subtract()
        print(f"The result of subtraction is: {result}")
    elif choice == "3":
        result = Multiply()
        print(f"The result of multiplication is: {result}")
    elif choice == "4":
        result = Divide()
        if result is not None:
            print(f"The result of division is: {result}")
    elif choice == "5":
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
    
    
    
    
