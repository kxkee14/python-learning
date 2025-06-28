
#scores 98 or average grade a
#score 80-89 grade B
#score 70-79 grade C
#score 60-69 grade D
#scores 60 or average Grade F

score = input("Please type your test score here: \n")
score = int(score)

if score >=98:
    print("congratulations your score is an A")
elif score >=80:
    print("your grade is a B")
elif score>=70:
    print("your grade is a C")
else:
    print("next time you should study more...")