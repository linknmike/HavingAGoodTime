quizCount = int(input("How many quizzes did you have? "))

quizGrades = 0
for i in range(quizCount):
    quizGrades += float(input("What was your score on quiz " + str(i + 1) + "? "))
quizGrades = quizGrades / quizCount
exam = float(input("What was your score on final exam? "))
finalGrade =  0.6 * exam + 0.4 * quizGrades
print("Your final grade percentage: " + str(finalGrade))
