max_poor_grades_count = int(input())
poor_grades_count = problem_count = total_score = 0
last_problem = ''

while True:
    problem_name = input()

    if problem_name == 'Enough':
        if problem_count > 0:
            print(f'Average score: {total_score / problem_count :.2f}')
            print(f'Number of problems: {problem_count}')
            print(f'Last problem: {last_problem}')
        break

    score = int(input())
    last_problem = problem_name

    problem_count += 1
    total_score += score

    if score <= 4:
        poor_grades_count += 1
        if poor_grades_count >= max_poor_grades_count:
            print(f'You need a break, {poor_grades_count} poor grades.')
            break
