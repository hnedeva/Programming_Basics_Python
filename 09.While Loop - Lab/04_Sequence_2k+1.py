input_number = int(input())
start_number = 1

while True:
    if start_number > input_number:
        break
    print(start_number)
    start_number = (2 * start_number) + 1
