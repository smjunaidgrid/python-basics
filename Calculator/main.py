num = float(input("Enter a number: "))
num1 = float(input("Enter another number: "))

print("Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = input("Choose an operation (1,2,3,4):")

if operation == '1':
    res = num + num1
    print(f"The addition of given numbers is : {res}")
elif operation == '2':
    res = num - num1
    print(f"The subtraction of given numbers is : {res}")
elif operation == '3':
    res = num * num1
    print(f"The multiplication of given numbers is : {res}")
elif operation == '4':
    if num1 != 0:
        res = num / num1
        print(f"The division of given numbers is : {res}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")
