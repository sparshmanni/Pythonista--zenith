

# Python program to print grades based on marks scored by a student
# given marks scored by student
given_marks = 68
markGrade = given_marks//10

# cheecking if grade greater than 9
if(markGrade >= 9):
    print("grade A+")
elif(markGrade < 9 and markGrade >= 8):
    print("grade A")
elif(markGrade < 8 and markGrade >= 7):
    print("grade B+")
elif(markGrade < 7 and markGrade >= 6):
    print("grade B")
elif(markGrade < 6 and markGrade >= 5):
    print("grade C+")
else:
    print("Fail")
