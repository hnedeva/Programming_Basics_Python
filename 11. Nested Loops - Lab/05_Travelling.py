while True:
    destination = input()
    if destination == 'End':
        break
    initial_budget = float(input())
    money = 0.0

    while money < initial_budget:
        new_income = float(input())
        money += new_income

    print(f'Going to {destination}!')

