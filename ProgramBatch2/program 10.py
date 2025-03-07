num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(*range(min(num1, num2) + 1, max(num1, num2)))
