# Take the input marks from user using input() function and find out the grade of the students. Note
#the grading will be in this manner – (100 – 91) – A1, (90-81) – A2, (80-71) – B1, (70-61) – B2, (60-
#51) – C1 (50-40) – C2 and less than 40 students will ‘Fail’. Also make sure user should input the
#marks in the range 0<=marks<=100, if user will input some other marks in should print invalid
#marks.


# 1st Approch 
def grade_of_students(marks):
    if marks >= 91 and marks <= 100:
        return ('your grade is A1')
    elif marks >= 81 and marks <= 90:
        return ('your grade is A2')
    elif marks >= 71 and marks <= 80:
        return ('your grade is B1')
    elif marks >= 61 and marks <= 70:
        return ('your grade is B2')
    elif marks >= 51 and marks <= 60:
        return ('your grade is c1')
    elif marks >= 40 and marks <=50:
        return ('your grade is c2')
    elif marks >=0 and marks < 40:
        return ('Fail')
    else:
        return("invalid")

marks = int(input('enter your marks to check your grade: '))
grade = grade_of_students(marks)
print(grade)

# 2nd Approch

def grade_of_students(marks):
    dict = { 4:"C2", 5:"C2", 6:"C1", 7:"B2",8 :"B1",9 :"A2",10 :"A1"}
    if marks < 40:
        return "Fail"
    key = marks // 10
    if marks % 10 > 0:
        key = key + 1
    return dict[key]
    
marks =int(input("enter the marks: "))
grade = grade_of_students(marks)
print(f"the grade of the student is : { grade}")