import math

planned_processors = int(input())
employees_count = int(input())
working_days = int(input())

processor_per_3h = 1
working_hours_per_day = 8
processor_price = 110.10

total_working_hours = employees_count * working_days * working_hours_per_day
processors_made = math.floor(total_working_hours / 3)
diff = processors_made - planned_processors

end_result = abs(diff) * processor_price

if processors_made >= planned_processors:
    print(f'Profit: -> {end_result:.2f} BGN')
else:
    print(f'Losses: -> {end_result:.2f} BGN')

