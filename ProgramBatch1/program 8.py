nums = [int(input("Enter a number: ")) for _ in range(10)]
print("Count of odd numbers:", sum(1 for n in nums if n % 2 != 0))
