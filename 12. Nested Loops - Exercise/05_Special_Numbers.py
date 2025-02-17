number = int(input())

result_string = ''
for n in range(1111, 9999 + 1):

    n_as_string = str(n)

    is_special = True
    for d in n_as_string:
        digit = int(d)

        if digit == 0:
            is_special = False
            break

        if number % digit != 0:
            is_special = False
            break

    if is_special:
        result_string += f'{n} '

print(result_string)