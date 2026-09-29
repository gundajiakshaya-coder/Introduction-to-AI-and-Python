name = input("Enter student name: ")

marks = []

for i in range(3):
    mark = float(input("Enter mark: "))
    marks.append(mark)

average = sum(marks) / len(marks)

print("\nStudent Name:", name)
print("Marks:", marks)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: F")