budget = float(input())
season = input()

place = location = ""
total_price = 0

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        location = "Alaska"
        total_price = 0.65 * budget
    elif season == "Winter":
        location = "Morocco"
        total_price = 0.45 * budget
elif 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        location = "Alaska"
        total_price = 0.80 * budget
    elif season == "Winter":
        location = "Morocco"
        total_price = 0.60 * budget
elif budget > 3000:
    place = "Hotel"
    total_price = 0.90 * budget
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"

print(f"{location} - {place} - {total_price:.2f}")
