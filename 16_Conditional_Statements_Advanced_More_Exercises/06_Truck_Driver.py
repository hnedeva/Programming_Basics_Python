season = input()
km_per_month = float(input())
salary = 0
price_per_km = 0

if season == "Spring" or season == "Autumn":
    if km_per_month <= 5000:
      price_per_km = 0.75
    elif 5000 < km_per_month <= 10_000:
        price_per_km = 0.95
    else:
        price_per_km = 1.45
elif season == "Summer":
    if km_per_month <= 5000:
      price_per_km = 0.90
    elif 5000 < km_per_month <= 10_000:
        price_per_km = 1.10
    else:
        price_per_km = 1.45
elif season == "Winter":
    if km_per_month <= 5000:
      price_per_km = 1.05
    elif 5000 < km_per_month <= 10_000:
        price_per_km = 1.25
    else:
        price_per_km = 1.45

salary_first = km_per_month * price_per_km * 4
salary = salary_first * 0.90

print(f"{salary:.2f}")