def GradeCalc():
    marks = float(input("Enter marks: "))
    if marks > 100 or marks < 0:
        Grade = "Invalid marks"
    elif marks >=90 and marks <=100:
        Grade = "A+"
    elif marks >=80 and marks <90:
        Grade = "A"
    elif marks >=70 and marks <80:
        Grade = "B"
    elif marks >=60 and marks <70:
        Grade = "C"
    elif marks >=50 and marks <60:
        Grade = "D"
    else:
        Grade = "F"
    return Grade, marks

grade, marks = GradeCalc()

if grade == "Invalid marks":
    print(grade)
else:
    print(f"Marks\t\tGrade\n---------------------\n{marks}\t\t{grade}")