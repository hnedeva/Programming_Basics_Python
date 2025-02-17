trip_cost = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

total_count = puzzles + talking_dolls + teddy_bears + minions + trucks
total_price = (puzzles * 2.60 +
               talking_dolls * 3 +
               teddy_bears * 4.10 +
               minions * 8.20 +
               trucks * 2)

discount = 0
if total_count >= 50:
    discount = 0.25

total_income = total_price * (1 - discount)
final_income = total_income * 0.90

if final_income >= trip_cost:
    money_left = final_income - trip_cost
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_needed = trip_cost - final_income
    print(f'Not enough money! {money_needed:.2f} lv needed.')