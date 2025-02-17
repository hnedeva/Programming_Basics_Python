actors_name = input()
initial_points = float(input())
num_judges = int(input())

total_points = initial_points

for _ in range(num_judges):
    judge_name = input()
    judge_score = float(input())

    points_awarded = (len(judge_name) * judge_score) / 2
    total_points += points_awarded

    if total_points >= 1250.5:
        print(f'Congratulations, {actors_name} got a nominee for leading role with {total_points :.1f}!')
        break
else:
    points_needed = 1250.5 - total_points
    print(f'Sorry, {actors_name} you need {points_needed :.1f} more!')
