num1 = int(input("Enter your first number\n"))
num2 = int(input("Enter your second number\n"))

operation = input("Choose an operation (+, -, *, /)\n")

def addNums(num1Input, num2Input):
    num1 = num1Input
    num2 = num2Input
    total = num1 + num2

    return f"Added numbers are {total}"

def subtractNum(num1Input, num2Input):
    num1 = num1Input
    num2 = num2Input
    total = num1 - num2

    return f"Subtracted numbers are {total}"

def multiplyNums(num1Input, num2Input):
    num1 = num1Input
    num2 = num2Input
    total = num1 * num2

    return f"Multiplied numbers are {total}"

def divideNums(num1Input, num2Input):
    num1 = num1Input
    num2 = num2Input
    if num2 == 0:
        return "You cannot divide by zero"

    total = num1 / num2

    return f"Divided numbers are {total}"

def performCalculation():
    match operation:
        case "+":
            print(addNums(num1, num2))
        case "-":
            print(subtractNum(num1, num2))
        case "*":
            print(multiplyNums(num1, num2))
        case "/":
            print(divideNums(num1, num2))
        case _:
            print("Invalid Operator")

performCalculation()