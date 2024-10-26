
# 1. Get the first test score.
# 2. get the second test score.
# 3. Get the third test score.
# 4. calculate the average by adding the three test score and dividing the sum by 3
# 5. display average if its greater then 95


Hight_score = 95

print("Test Average".center(160))
test_1 = float(input("Enter the First test score: "))
test_2 = float(input("Enter the Second test score: "))
test_3 = float(input("Enter the Third test score: "))

test_average = (test_1 + test_2 + test_3) / 3

print("The average score is ", round(test_average, 2))


# if the average is high score

if test_average >= Hight_score:
    print("Congratulations!")
    print("That is a great average", test_average)