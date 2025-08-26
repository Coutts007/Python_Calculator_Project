first_Number=input("Enter the first number: ")
second_Number=input("Enter the second number: ")
operater=input("Enter the operator (+, -, *, /): ")
if operater == "+":
    result = float(first_Number) + float(second_Number)
elif operater == "-":
    result = float(first_Number) - float(second_Number)
elif operater == "*":
    result = float(first_Number) * float(second_Number)
elif operater == "/":
    if float(second_Number) != 0: 
        result = float(first_Number) / float(second_Number)
    else:
        result = "Error: Division by zero is not allowed."
print(result)