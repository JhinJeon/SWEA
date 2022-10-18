# 반반

t = int(input())

for tc in range(1, t+1):
    s = input()
    overlap_list = []
    answer = 'Yes'
    for spell in s:
        if spell not in overlap_list:
            overlap_list.append(spell)
        elif overlap_list.count(spell) > 2:
            answer = 'No'
            break

    if len(overlap_list) != 2:
        answer = 'No'

    print(f'#{tc} {answer}')
