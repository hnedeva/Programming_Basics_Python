projection_type = input()
rows = int(input())
columns = int(input())
income = 0.0
cinema_capacity = columns * rows

if projection_type == 'Premiere':
    income = cinema_capacity * 12
elif projection_type == 'Normal':
    income = cinema_capacity * 7.50
elif projection_type == 'Discount':
    income = cinema_capacity * 5

print(f'{income :.2f} leva')