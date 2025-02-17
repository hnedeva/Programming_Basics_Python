number = int(input())

bonus = 0
if number <= 100:
    bonus = 5
elif number <= 1000:
    bonus = number * 0.20
else:
    bonus = number * 0.10

additional_bonus = 0
if number % 2 == 0:
    additional_bonus = 1
if number % 10 == 5:
    additional_bonus = 2

total_bonus = bonus + additional_bonus

print(total_bonus)
print(number + total_bonus)