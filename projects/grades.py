
# This program gets a numeric test score from the user
# display the corresponding Letter grade



# named constants to represent the grade 

A_score = 90
B_score = 80
C_score = 70
D_score = 60

student_score = int(input('Enter the test score: '))

if student_score >= A_score:
    print('Your grade is A')
else:
    if student_score >= B_score:
        print('Your grade is B')
    else:
        if student_score >= C_score:
            print('Your garde is C')
        else:
            if student_score >= D_score:
                print('Your score is D')
            else:
                print('Your grade is F')                


# if student_score >= A_score:
#     print('Your grade is A')
# elif student_score >= B_score:
#     print('Your grade is B')
# elif student_score >= C_score:
#     print('Your garde is C')
# elif student_score >= D_score:
#     print('Your score is D')
# else:
#     print('Your grade is F')    
