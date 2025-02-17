width = int(input())
length = int(input())
height = int(input())

box_size = width * length * height

while True:
    command = input()
    if command == 'Done':
        break
    current_boxes = int(command)
    box_size -= current_boxes

    if box_size <= 0:
        break

if box_size >= 0:
    print(f'{box_size} Cubic meters left.')
else:
    print(f'No more free space! You need {-box_size} Cubic meters more.')
