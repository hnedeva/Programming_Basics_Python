age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

total_money = 0
total_toys = 0

for bd in range(1, age + 1):
    if bd % 2 == 0:
        total_money += bd * 5
        total_money -= 1
    else:
        total_toys += 1

total_toys_price = total_toys * toy_price
total_total = total_toys_price + total_money

if total_total >= washing_machine_price:
    enough_money = total_total - washing_machine_price
    print(f'Yes! {enough_money :.2f}')
else:
    money_needed = washing_machine_price - total_total
    print(f'No! {money_needed :.2f}')
