import sys

numbers_count = int(input())

total_sum = 0
biggest_num = -sys.maxsize

for _ in range(numbers_count):
    current_number = int(input())

    total_sum += current_number
    if current_number > biggest_num:
        biggest_num = current_number

if biggest_num == total_sum - biggest_num:
    print('Yes')
    print(f'Sum = {biggest_num}')
else:
    diff = abs(biggest_num - (total_sum - biggest_num))
    print('No')
    print(f'Diff = {diff}')