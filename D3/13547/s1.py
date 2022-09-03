# 팔씨름

t = int(input())

for tc in range(1, t+1):
    record = str(input())
    win = 0
    lose = 0
    remains = 15 - len(record)

    for r in record:
        if r == 'o':
            win += 1
        else:
            lose += 1

    if win + remains >= 8:
        answer = 'YES'
    else:
        answer = 'NO'

    print(f'#{tc} {answer}')
