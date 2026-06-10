studentName = input("Enter your name: ")
studentMark = int(input("Enter your mark: "))
if studentMark >= 90:
    print("Grade : A")
elif studentMark >= 80:
    print("Grade: B")
elif studentMark >= 70:
    print("Grade: C")
elif studentMark >= 60:
    print("Grade: D")
else:
    print("Grade: E")

if studentMark >= 40:
    print("Pass")
else:
    print("Fail")