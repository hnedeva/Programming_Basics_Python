import math

record_in_seconds = float(input())
distance = float(input())
time_for_1_m = float(input())

slowdown = math.floor(distance / 15) * 12.5
swimming_seconds = distance * time_for_1_m

total_time = swimming_seconds + slowdown

if total_time < record_in_seconds:
    print(f' Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    seconds_needed = total_time - record_in_seconds
    print(f'No, he failed! He was {seconds_needed:.2f} seconds slower.')
