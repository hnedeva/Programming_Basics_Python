flower_type = input()
flower_count = int(input())
budget = int(input())
flower_price = 0.0
discount = 0.0

if flower_type == 'Roses':
    flower_price = 5
    if flower_count > 80:
        discount = 0.10
elif flower_type == 'Dahlias':
    flower_price = 3.80
    if flower_count > 90:
        discount = 0.15
elif flower_type == 'Tulips':
    flower_price = 2.80
    if flower_count > 80:
        discount = 0.15
elif flower_type == 'Narcissus':
    flower_price = 3
    if flower_count < 120:
        discount = -0.15
elif flower_type == 'Gladiolus':
    flower_price = 2.50
    if flower_count < 80:
        discount = -0.20

total_price = flower_price * flower_count * (1 - discount)

if budget >= total_price:
    money_left = budget - total_price
    print(f'Hey, you have a great garden with {flower_count} {flower_type} and {money_left :.2f} leva left.')
else:
    money_needed = total_price - budget
    print(f'Not enough money, you need {money_needed :.2f} leva more.')