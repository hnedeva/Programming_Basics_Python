import sys

min_number = sys.maxsize

while True:
    command_or_number = input()
    if command_or_number == 'Stop':
        break
    number = int(command_or_number)
    if number < min_number:
        min_number = number

print(min_number)