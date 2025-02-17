locations_count = int(input())

for _ in range(locations_count):
    expected_gold = float(input())
    days = int(input())

    total_gold = 0
    for _ in range(days):
        total_gold += float(input())

    average_gold_per_day = total_gold / days
    if average_gold_per_day >= expected_gold:
        print(f'Good job! Average gold per day: {average_gold_per_day:.2f}.')
    else:
        gold_needed = expected_gold - average_gold_per_day
        print(f'You need {gold_needed:.2f} gold.')