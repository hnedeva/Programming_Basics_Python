import math

average_speed = float(input())
litres_per_100km = float(input())

moon_distance = 384400

total_distance = moon_distance * 2
travel_time = total_distance / average_speed
travel_time = math.ceil(travel_time)
total_time = travel_time + 3
total_fuel = (litres_per_100km * total_distance) / 100

print(total_time)
print(f'{total_fuel:.0f}')