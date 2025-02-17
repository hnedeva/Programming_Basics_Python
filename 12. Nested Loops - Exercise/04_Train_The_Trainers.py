judges_count = int(input())

total_sum = 0
presentation_count = 0
command = input()
while command != 'Finish':
    current_presentation = command
    presentation_count += 1

    current_sum = 0
    for _ in range(judges_count):
        judge_score = float(input())
        current_sum += judge_score

    avg_score = current_sum / judges_count
    print(f'{current_presentation} - {avg_score :.2f}.')

    total_sum += current_sum

    command = input()

total_avg_score = total_sum / (judges_count * presentation_count)
print(f'Student\'s final assessment is {total_avg_score :.2f}.')