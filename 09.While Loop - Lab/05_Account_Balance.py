new_money = input()
total_sum = 0

while new_money != 'NoMoreMoney':
    number_from_input = float(new_money)
    if number_from_input < 0:
        print('Invalid operation!')
        break
    print(f'Increase: {number_from_input :.2f}')
    total_sum += number_from_input
    new_money = input()

print(f'Total: {total_sum :.2f}')

