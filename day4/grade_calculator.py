studentName = input("Enter your name: ")
studentMark  = int(input("Enter your mark: "))
print('\n')
if studentMark >= 90:
    print("Your Grade is A")
elif studentMark >= 80:
    print("Your Grade is B")
elif studentMark >= 60:
    print("Your Grade is C")
else:
    print("You are failed")
