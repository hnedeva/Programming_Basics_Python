budget = int(input())
season = input()
fisherman = int(input())
rent = 0
discount = 0.0

if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

if fisherman <= 6:
    discount = 0.10
elif fisherman <= 11:
    discount = 0.15
else:
    discount = 0.25

additional_discount = 0.0

if fisherman % 2 == 0 and season != 'Autumn':
    additional_discount = 0.05

total = rent * (1 - discount) * (1 - additional_discount)

if budget >= total:
    money_left = budget - total
    print(f'Yes! You have {money_left :.2f} leva left.')
else:
    money_needed = total - budget
    print(f'Not enough money! You need {money_needed :.2f} leva.')
