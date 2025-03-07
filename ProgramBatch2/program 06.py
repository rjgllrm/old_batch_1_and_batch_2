numbers = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
print("Result:", numbers[0] - sum(numbers[1:]))
