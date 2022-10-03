# 프리셀
import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t + 1):
    # memory = 기억하는 플레이한 게임 수
    # winrate_today = 오늘 승률
    # winrate_total = 누적 승률
    memory, winrate_today, winrate_total = map(int, input().split())
    answer = 'Broken'
    win_today = int(winrate_today * memory / 100)
    lose_today = memory - win_today

    # 1. 오늘 승리 횟수를 정수값으로 산출할 수 있는지 확인
    for m in range(1, memory+1):
        wintime = int(m * winrate_today / 100)
        if m * winrate_today / 100 == wintime:
            answer ='Possible'
            break

    # 2. 오늘 패배한 적이 있는데 누적 승률이 100%이거나 오늘 승리한 적이 있는데 누적 승률이 0%인 경우 == 불가능
    if winrate_total == 100 and lose_today > 0 or winrate_total == 0 and winrate_today > 1:
        answer = 'Broken'
    print(f'#{tc} {answer}')

