student_name = input()
grade = 1
score = max_tries = 0

while True:
    new_score = float(input())
    if new_score < 4:
        max_tries += 1
        if max_tries > 1:
            print(f'{student_name} has been excluded at {grade} grade')
            break
        continue
    score += new_score
    if grade == 12:
        print(f'{student_name} graduated. Average grade: {score / 12 :.2f}')
        break
    grade += 1
