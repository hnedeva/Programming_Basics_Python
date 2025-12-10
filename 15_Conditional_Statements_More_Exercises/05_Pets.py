import math

days = int(input())
food_left_kg = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_kg = float(input())

total_food = (days * dog_food_per_day_kg
              + days * cat_food_per_day_kg
              + days * (turtle_food_per_day_kg / 1000))

if food_left_kg >= total_food:
    left_over = food_left_kg - total_food
    print(f"{math.floor(left_over)} kilos of food left.")
else:
    kg_needed = total_food - food_left_kg
    print(f"{math.ceil(kg_needed)} more kilos of food are needed.")
