free_days = int(input())

tom_norm_play = 30000

work_days = 365 - free_days
in_work_days_in_min = work_days * 63
in_free_days_in_min = free_days * 127

play_time = in_free_days_in_min + in_work_days_in_min

if play_time > tom_norm_play:
    diff = play_time - tom_norm_play
    difference_hours = diff // 60
    difference_minutes = diff % 60
    print("Tom will run away")
    print(f"{difference_hours} hours and {difference_minutes} minutes more for play")
else:
    diff = tom_norm_play - play_time
    total_hours = diff // 60
    total_minutes = diff % 60
    print("Tom sleeps well")
    print(f"{total_hours} hours and {total_minutes} minutes less for play")
