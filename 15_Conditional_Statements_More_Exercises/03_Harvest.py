import math

x = int(input()) # кв.м е лозето
y = float(input()) # грозде за един кв.м
z = int(input()) # нужни литри вино
workers = int(input())

grapes_needed_1_litre = 2.5

grapes_for_wine = x * y * 0.40
total = grapes_for_wine / grapes_needed_1_litre

if total < z:
    wine_needed = z - total
    print(f"It will be a tough winter! More {math.floor(wine_needed)} liters wine needed.")
else:
    wine_left = total - z
    wine_per_worker = wine_left / workers
    print(f'Good harvest this year! Total wine: {math.floor(total)} liters.')
    print(f"{math.ceil(wine_left)} liters left -> {math.ceil(wine_per_worker)} liters per person.")