n = int(input())
left_sum = right_sum = 0

for idx in range(2 * n):
    new_number = int(input())
    if idx < n:
       left_sum += new_number
    else:
        right_sum += new_number

if right_sum == left_sum:
    print(f'Yes, sum = {right_sum}')
else:
    print(f'No, diff = {abs(right_sum - left_sum)}')