print("Student report")
print("--------------")

name  = input("Name : ")
roll_no =  int(input("Roll no. : "))

marks = []

for i in range(5):
    item = int(input(f"enter marks {i+1}: "))
    marks.append(item)

print("\nMarks :", marks)

total = sum(marks)
avg = sum(marks)/len(marks)
max = max(marks)
min = min(marks)

print("Total : ", total)
print("Average : ", avg)
print("Highest : ", max)
print("Lowest : ", min)

if (avg >= 90):
    print("Grade : A ")
    print("Remark : Excelent")
elif (avg >= 80):
    print("Grade : B ")
    print("Remark : Good ")

elif (avg >= 60):
    print("Grade : C")
    print("Remark : Fair")  

else:
    print("Grade : D")