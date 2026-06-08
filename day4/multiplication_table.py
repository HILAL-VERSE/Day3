number = int(input("Enter a number to multiply: "))

print(f"\nMultiplication Table for {number}: ")

for i in range(1, 11):
     result = number * i
     print(f"{number} x {i} = {result}")
