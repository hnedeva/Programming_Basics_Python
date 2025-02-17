nailon = int(input())
paint = int(input())
litres_razreditel = int(input())
hours = int(input())

nailon_additional = nailon + 2
paint_additional = paint * 1.10

total_material = nailon_additional * 1.50 + paint_additional * 14.50 + litres_razreditel * 5 + 0.40
payment_maistori_per_hour = total_material * 0.30 * hours
total = total_material + payment_maistori_per_hour

print(total)