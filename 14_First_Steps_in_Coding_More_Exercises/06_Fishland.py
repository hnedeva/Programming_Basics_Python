skumria_price_per_kg = float(input())
caca_price_per_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

palamud_price_per_kg = skumria_price_per_kg * 1.60
safrid_price_per_kg = caca_price_per_kg * 1.80
midi_price_per_kg = 7.50

total_price = (palamud_price_per_kg * palamud_kg
               + safrid_price_per_kg * safrid_kg
               + midi_price_per_kg * midi_kg)

print(f"{total_price:.2f}")
