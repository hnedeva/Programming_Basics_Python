tournament_count = int(input())
initial_points = int(input())
tournaments_win = 0
points_gained = 0

for _ in range(tournament_count):
    stage_of_tournament = input()
    if stage_of_tournament == 'W':
        points_gained += 2000
        tournaments_win += 1
    elif stage_of_tournament == 'F':
        points_gained += 1200
    elif stage_of_tournament == 'SF':
        points_gained += 720

final_points = initial_points + points_gained
average_points = points_gained // tournament_count
percentage = tournaments_win / tournament_count * 100

print(f'Final points: {final_points}')
print(f'Average points: {average_points}')
print(f'{percentage :.2f}%')