# w.a.p that calculates and displays the letter grade for a given numerical score
# (ex:- A, B,C,D or F) based on the following grading scale:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
    print('You are in grade: A')
elif score >= 80 and score <= 89:
    print('You are in grade: B')
elif score >= 70 and score <= 79:
    print('You are in grade: C')
elif score >= 60 and score <= 69:
    print('You are in grade: D')
elif score > 100  or score <= -1:
    print('You are a superman! you can get a grade! : 0')
else:
    print('You are in grade: F')