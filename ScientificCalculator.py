import math

calculations = 0
currentResult = 0.0
totalResult = 0.0

def print_menu():
    print("Calculator Menu")
    print("---------------")
    print("0. Exit Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Logarithm")
    print("7. Display Average\n")

def display_stats(numCalcs, sumCalcs):
    print("Sum of calculations:", sumCalcs)
    print("Number of calculations:", numCalcs)
    print(f"Average of calculations: {sumCalcs/numCalcs:.2f}")

def get_input():
    choice = ""
    operand1 = 0
    operand2 = 0
    validMenu = False
    validOperands = False
    while not (validMenu and validOperands):

        #Repeat until menu option is valid
        if not validMenu:
            choice = input("Enter Menu Selection: ")
            if choice not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
                print("Error: Invalid selection!")
                continue
            else:
                validMenu = True

        #Repeat until operands are valid
        if not validOperands:
            if choice in ["1", "2", "3", "4", "5", "6"]:

                operand1 = input("Enter first operand: ")
                if operand1 == "RESULT":
                    operand1 = currentResult
                else:
                    operand1 = float(operand1)

                operand2 = input("Enter second operand: ")
                if operand2 == "RESULT":
                    operand2 = currentResult
                else:
                    operand2 = float(operand2)

                if choice == "4":
                    if operand2 != 0:
                        validOperands = True
                    else:
                        print("Error: invalid input!")
                elif choice == "6":
                    if operand1 > 0 and operand2 > 0:
                        validOperands = True
                    else:
                        print("Error: invalid input!")
                elif choice == "5":
                    if operand1 != 0 and operand2 != 0:
                        if operand1 < 0 and operand2 % 1 == 0:
                            validOperands = True
                        elif operand1 >= 0:
                            validOperands = True
                        else:
                            print("Error: invalid input!")
                else:
                    validOperands = True
            else:
                validOperands = True
    return choice, operand1, operand2

print("Current Result:", currentResult)
print_menu()

while True:

    menuOption, operand1, operand2 = get_input()

    if menuOption == "0":
        print("Thanks for using this calculator. Goodbye!")
        break
    elif menuOption == "1":
        currentResult = (operand1 + operand2)
        calculations += 1
    elif menuOption == "2":
        currentResult = (operand1 - operand2)
        calculations += 1
    elif menuOption == "3":
        currentResult = (operand1 * operand2)
        calculations += 1
    elif menuOption == "4":
        currentResult = (operand1 / operand2)
        calculations += 1
    elif menuOption == "5":
        currentResult = (operand1 ** operand2)
        calculations += 1
    elif menuOption == "6":
        currentResult = (math.log(operand2, operand1))
        calculations += 1
    elif menuOption == "7":
        if calculations == 0:
            print("Error: No calculations yet to average!")
            continue
        else:
            display_stats(calculations, totalResult)
            continue

    print("Current Result: ", currentResult)
    totalResult += currentResult

    print_menu()
