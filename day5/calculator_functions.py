def addition(num1, num2):
    result = num1 + num2
    return result

def substraction(num1, num2):
    result = num1 - num2
    return result

def multiplication(num1, num2):
    result = num1 * num2
    return result

def division(num1, num2):
    if num2 != 0:
        result = num1 / num2
        return result
    else:
        error = "Cannot divide by zero"
        return error
    return result
 

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
choice = input("Enter operaotr : ")

if choice == "+":
    result = addition(number1, number2)
    print(result)
elif choice == "-":
    result = substraction(number1, number2)
    print(result)
elif choice == "*":
    result = multiplication(number1, number2)
    print(result)
elif choice ==  "/":
    result = division(number1, number2)
    print(result)
else:
    print("Invalid Operator")
    

