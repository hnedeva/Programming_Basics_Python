n = int(input())
sum_odd = sum_even = 0

for idx in range(n):
    new_number = int(input())
    if idx % 2 == 0:
        sum_even += new_number
    elif idx % 2 != 0:
        sum_odd += new_number

if sum_odd == sum_even:
    print(f'Yes')
    print(f'Sum = {sum_odd}')
else:
    print('No')
    print(f'Diff = {abs(sum_odd - sum_even)}')