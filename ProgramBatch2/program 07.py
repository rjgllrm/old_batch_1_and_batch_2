numbers = [float(input(f"Enter number {i+1}: ")) for i in range(10)]
print("Count of even numbers:", sum(1 for n in numbers if n % 2 == 0))
