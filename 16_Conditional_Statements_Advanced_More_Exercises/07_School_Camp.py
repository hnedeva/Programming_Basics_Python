season = input()
group_type = input() # “boys”, “girls” или “mixed”;
students_count = int(input())
nights_count = int(input())

sport_type = ""
total_price = 0
night_price = 0

if season == "Winter":
    if group_type == "boys":
        night_price = 9.60
        sport_type = "Judo"
    elif group_type == "girls":
        night_price = 9.60
        sport_type = "Gymnastics"
    elif group_type == "mixed":
        night_price = 10
        sport_type = "Ski"
elif season == "Spring":
    if group_type == "boys":
        night_price = 7.20
        sport_type = "Tennis"
    elif group_type == "girls":
        night_price = 7.20
        sport_type = "Athletics"
    elif group_type == "mixed":
        night_price = 9.50
        sport_type = "Cycling"
elif season == "Summer":
    if group_type == "boys":
        night_price = 15
        sport_type = "Football"
    elif group_type == "girls":
        night_price = 15
        sport_type = "Volleyball"
    elif group_type == "mixed":
        night_price = 20
        sport_type = "Swimming"

total_price = students_count * night_price * nights_count

if students_count >= 50:
    total_price *= 0.50
elif 20 <= students_count < 50:
    total_price *= 0.85
elif 10 <= students_count < 20:
    total_price *= 0.95


print(f"{sport_type} {total_price:.2f} lv.")