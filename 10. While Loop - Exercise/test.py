steps_goal = 10_000
total_steps = 0

while True:
    command = input()
    if command == 'Going home':
        extra_steps = int(input())
        total_steps += extra_steps
        break

    current_steps = int(command)
    total_steps += current_steps

    if total_steps >= steps_goal:
        print('Goal reached! Good job!')
        diff_over = total_steps - steps_goal
        print(f'{diff_over} steps over the goal!')
        break

if total_steps < steps_goal:
    diff_under = steps_goal - total_steps
    print(f'{diff_under} more steps to reach goal.')