food_quantity_in_kg = int(input()) * 1000
total_food = 0

while True:
    food = input()
    if food == "Adopted":
        break
    total_food += int(food)

if food_quantity_in_kg >= total_food:
    print(f"Food is enough! Leftovers: {food_quantity_in_kg - total_food} grams.")
else:
    print(f"Food is not enough. You need {total_food - food_quantity_in_kg} grams more.")
