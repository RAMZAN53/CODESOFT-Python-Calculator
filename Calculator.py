class Calculation:
    def Addition(self, num1, num2):
        result = int(num1) + int(num2)
        print("ADDITION OF NUMBERS IS : " + str(result))

    def Subtraction(self, num1, num2):
        result = int(num1) - int(num2)
        print("SUBTRACTION OF NUMBERS IS : " + str(result))

    def Multiplication(self, num1, num2):
        result = int(num1) * int(num2)
        print("MULTIPLICATION OF NUMBERS IS : " + str(result))

    def Division(self, num1, num2):
        if num2 == '0':
            print("ERROR -> CANNOT DIVIDE TO ZERO")
        else:
            result = int(num1) / int(num2)
            print("DIVISION OF NUMBERS IS : " + str(result))

print("\t \t \t >>> CALCULATOR <<< ")
cal = Calculation()
while True:
    number1 = input("ENTER NUMBER 1: ")
    number2 = input("ENTER NUMBER 2: ")
    operator = input("ENTER OPERATOR (+, -, *, /): ")

    if operator == "+":
        cal.Addition(number1, number2)
    elif operator == "-":
        cal.Subtraction(number1, number2)
    elif operator == "*":
        cal.Multiplication(number1, number2)
    elif operator == "/":
        cal.Division(number1, number2)
    else:
        print("Invalid operator")

    choice = input("DO YOU WANT TO CONTINUE? (YES/NO): ")
    if choice == "NO": 
        break
