#Python_Calculating GPA using While Loop
"Computer Programming Tutor,Aug 19,2021"

gradingScale = { "A":4,"B":3,"C":2,"D":1,"F":0}
num = int(input("How Many GPA's would you like to Calculate?:"))

while num:
    n = int(input("How Many Courses will you input?: "))
    Tpoints = 0
    Tunits = 0
    while n:
        grade = input("Enter Grade for Course: ")
        units = int(input("How Many Units was the Course?:"))
        Tunits += units
        points = gradingScale[grade]*units
        Tpoints += points
        n -= 1

    GPA = float(Tpoints)/ Tunits
    print("GPA is :",("%.2f"%GPA))
    print("Total Points = ",Tpoints)
    print("Total Units =",Tunits)
    num -= 1
    
