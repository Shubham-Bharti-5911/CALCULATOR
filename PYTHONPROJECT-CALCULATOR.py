#calculator using python coding for project

def addition(num1,num2):
    result = num1+num2
    print("Sum is :",result)

def subtraction(num1,num2):
    result = num1-num2
    print("Subtraction is :",result)

def multiplication(num1,num2):
    result = num1 * num2
    print("Multiplication is :", result)

def division(num1,num2):
    if num2 == 0.0:
        print("Can't Do Divide by Zero")
    else:
        result = num1 / num2
        print("Division is:", result)

while True:
    print("What do you want to do?")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("ENTER q OR Q TO EXIT")

    choice=input("ENTER YOUR CHOICE:")

    if choice == 'Q' or choice== 'q':
        break

    num1=float(input("Enter Number 1: "))
    num2=input("Enter Number 2: ")
    if choice == '1':
        addition(num1,num2)
    elif choice == '2':
        subtraction(num1,num2)
    elif choice=='3':
        multiplication(num1,num2)
    elif choice=='4':
        division(num1,num2)
    else:
        print("INVALID CHOICE")

print("mini proj")