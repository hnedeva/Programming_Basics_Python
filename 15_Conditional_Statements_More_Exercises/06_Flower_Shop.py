import math

magnolia_count = int(input())
zumbuls_count = int(input())
roses_count = int(input())
cactus_count = int(input())
present_price = float(input())

total = (magnolia_count * 3.25
         + zumbuls_count * 4
         + roses_count * 3.50
         + cactus_count * 8)

taxes = total * 0.05
final_price = total - taxes

if final_price >= present_price:
    money_left = final_price - present_price
    print(f"She is left with {math.floor(money_left)} leva.")
else:
    money_needed = present_price - final_price
    print(f"She will have to borrow {math.ceil(money_needed)} leva.")
