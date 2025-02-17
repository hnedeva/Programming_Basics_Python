budget = float(input())
statists_count = int(input())
clothes = float(input())

decor = budget * 0.10

if statists_count > 150:
    clothes *= 0.90

total_clothes_price = statists_count * clothes
total_cost = decor + total_clothes_price

if total_cost > budget:
    money_needed = total_cost - budget
    print(f'Not enough money!')
    print(f'Wingard needs {money_needed:.2f} leva more.')
else:
    money_left = budget - total_cost
    print(f'Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')

