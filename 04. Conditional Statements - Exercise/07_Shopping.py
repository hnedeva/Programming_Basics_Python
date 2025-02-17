budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

video_cards_price = video_cards * 250
processors_price = video_cards_price * 0.35
ram_price = video_cards_price * 0.10

total_price = video_cards_price + processors_price * processors + ram_price * ram

if video_cards > processors:
    total_price *= 0.85

if budget >= total_price:
    money_left = budget - total_price
    print(f'You have {money_left:.2f} leva left!')
else:
    money_needed = total_price - budget
    print(f'Not enough money! You need {money_needed:.2f} leva more!')
