operation = input("Please specify the operation you would like to perform (add, sub, multiply, divide): ")

def add(num1, num2):
    add_result = num1 + num2
    return add_result

def sub(num1, num2):
    sub_result = num1 - num2
    return sub_result

def multiply(num1, num2):
    mul_result = num1 * num2
    return mul_result

def divide(num1, num2):
    div_result = num1/num2
    return div_result

num1 = float(input ("Input Number: "))
num2 = float(input ("Second number: "))

if operation == "add":
    print(add(num1, num2))
elif operation == "sub":
    print(sub(num1, num2))
elif operation == "multiply":
    print(multiply(num1, num2))
elif operation == "divide":
    print(divide(num1, num2))
else:
    print ("Incorrect operation. Please choose correct value.")