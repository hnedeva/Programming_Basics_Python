veggies_per_kilo = float(input())
fruits_per_kilo = float(input())
veggies_total = int(input())
fruits_total = int(input())

total_income = (veggies_per_kilo * veggies_total + fruits_per_kilo * fruits_total) / 1.94

print(f"{total_income:.2f}")
