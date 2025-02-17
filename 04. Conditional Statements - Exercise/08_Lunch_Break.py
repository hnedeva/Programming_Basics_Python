import math

name = input()
duration_episode = int(input())
duration_break = int(input())

lunch_time = duration_break / 8
rest_time = duration_break / 4
time_left = duration_break - lunch_time - rest_time
time_free = time_left - duration_episode

if time_left >= duration_episode:
    print(f'You have enough time to watch {name} and left with {math.ceil(time_free)} minutes free time.')
else:
    time_needed = duration_episode - time_left
    print(f"You don't have enough time to watch {name}, you need {math.ceil(time_needed)} more minutes.")
