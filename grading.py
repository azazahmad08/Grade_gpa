'''
In This program we will count someone grade based on there result 
Note that this grading system is used all over the world and usally marks may varri incase of pass or fail'''

mark = int(input("Enter your mark:"))

if mark>=80:
    print("A+")
elif mark>=70:
    print("A")
elif mark>=60:
    print("A-")
elif mark>=50:
    print("B")
elif mark>=40:
    print("C")
elif mark>=33:
    print("D")
else:
    print("Fail")

#Run this program and you will find your desire grade according to your mark
#Note: This depend on your grade system: