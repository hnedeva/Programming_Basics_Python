hours = int(input())
minutes = int(input())

minutes_plus = minutes + 15
if minutes_plus >= 60:
    minutes_plus -= 60
    hours += 1
if hours == 24:
    hours = 00

print(f'{hours}:{minutes_plus :02d}')