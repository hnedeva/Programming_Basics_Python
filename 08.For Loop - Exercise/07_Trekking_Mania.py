group_count = int(input())

musala = 0
monblanc = 0
kilimandjaro = 0
k2 = 0
everest = 0

total_climbers = 0

for _ in range(0, group_count):
    people_in_group = int(input())
    total_climbers += people_in_group
    if people_in_group <= 5:
        musala += people_in_group
    elif people_in_group <= 12:
        monblanc += people_in_group
    elif people_in_group <= 25:
        kilimandjaro += people_in_group
    elif people_in_group <= 40:
        k2 += people_in_group
    else:
        everest += people_in_group

print(f'{(musala / total_climbers) * 100:.2f}%')
print(f'{(monblanc / total_climbers) * 100:.2f}%')
print(f'{(kilimandjaro / total_climbers) * 100:.2f}%')
print(f'{(k2 / total_climbers) * 100:.2f}%')
print(f'{(everest / total_climbers) * 100:.2f}%')