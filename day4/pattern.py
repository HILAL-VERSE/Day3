for i in range(1,5):
    print("*"*i)

for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

letters = ["A","B","C","D","E"]
for row in range(1, 6):
    for index in range(0, row):
        print(letters[index], end="")
    print()

for i in range(1,5):
    print("5"*i)

for row in range(5, 0, -1):
    
    for index in range(0, row):
        print("*", end="")
        
    print()