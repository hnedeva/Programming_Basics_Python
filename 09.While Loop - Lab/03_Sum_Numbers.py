initial_number = int(input())
total_sum = 0

while True:
    new_number = int(input())
    total_sum += new_number
    if total_sum >= initial_number:
        break

print(total_sum)