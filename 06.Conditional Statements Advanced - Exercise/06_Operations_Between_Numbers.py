number_1 = int(input())
number_2 = int(input())
operator_type = input()
result = 0.0
even_or_odd = ''

if operator_type == '+':
    result = number_1 + number_2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{number_1} {operator_type} {number_2} = {result} - {even_or_odd}')
elif operator_type == '-':
    result = number_1 - number_2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{number_1} {operator_type} {number_2} = {result} - {even_or_odd}')
elif operator_type == '*':
    result = number_1 * number_2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{number_1} {operator_type} {number_2} = {result} - {even_or_odd}')
elif operator_type == '/':
    if number_2 == 0:
        print(f'Cannot divide {number_1} by zero')
    else:
        result = number_1 / number_2
        print(f'{number_1} / {number_2} = {result :.2f}')
elif operator_type == '%':
    if number_2 == 0:
        print(f'Cannot divide {number_1} by zero')
    else:
        result = number_1 % number_2
        print(f'{number_1} % {number_2} = {result}')
