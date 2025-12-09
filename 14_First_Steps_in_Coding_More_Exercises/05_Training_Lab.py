from math import floor

w = float(input())
h = float(input())


h_in_cm = (h * 100) - 100
w_in_cm = w * 100

desks_per_row = (floor(h_in_cm / 70))
rows = floor(w_in_cm / 120)

seats = (desks_per_row * rows) - 3

print(seats)
