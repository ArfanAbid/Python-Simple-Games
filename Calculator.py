import os
import time

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculator():
    i=0
    name="\t\t\t\t\t\t Welcome to the Calculator ~ CASIO ~ "
    for i in name:
      time.sleep(0.2)
      print(i,end='')
    
    print()

    while True:
                             
        print("Select an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
      
        choice = input("Enter your choice (1-5): ")


        if choice == '5':
            print("Thank you for using the Calculator!")
            break
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
            print("The result is:", result)
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == '2':
            result = subtract(num1, num2)
            print("The result is:", result)
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == '3':
            result = multiply(num1, num2)
            print("The result is:", result)
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero!")
                time.sleep(5)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                result = divide(num1, num2)
                print("The result is:", result)
                time.sleep(5)
                os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Invalid choice. Please try again.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

# Run the calculator
calculator()
