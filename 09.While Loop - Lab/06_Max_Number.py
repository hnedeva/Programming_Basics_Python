import sys

max_number = -sys.maxsize

while True:
    command_or_number = input()
    if command_or_number == 'Stop':
        break
    number = int(command_or_number)
    if number > max_number:
        max_number = number
print(max_number)
