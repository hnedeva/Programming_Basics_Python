hrizantemi_count = int(input())
roses_count = int(input())
laleta_count = int(input())
season = input()
holiday_or_not = input()

if season == "Spring" or season == "Summer":
    hrizantemi_price = 2
    roses_price = 4.10
    laleta_price = 2.50
else:
    hrizantemi_price = 3.75
    roses_price = 4.50
    laleta_price = 4.15

flower_sum = (hrizantemi_count * hrizantemi_price +
              roses_count * roses_price +
              laleta_count * laleta_price)

if holiday_or_not == "Y":
    flower_sum *= 1.15
if season == "Spring" and laleta_count > 7:
    flower_sum *= 0.95
if season == "Winter" and roses_count >= 10:
    flower_sum *= 0.90

total_count = hrizantemi_count + roses_count + laleta_count
if total_count > 20:
    flower_sum *= 0.80

final_price = flower_sum + 2

print(f"{final_price:.2f}")
