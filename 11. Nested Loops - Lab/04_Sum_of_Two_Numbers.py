start = int(input())
end = int(input())
magic_number = int(input())
counter = 0
found = False

for num_1 in range(start, end + 1):
    for num_2 in range(start, end + 1):
        counter += 1
        if num_1 + num_2 == magic_number:
            found = True
            print(f'Combination N:{counter} ({num_1} + {num_2} = {magic_number})')
            break

    if found:
        break

if not found:
    print(f'{counter} combinations - neither equals {magic_number}')
