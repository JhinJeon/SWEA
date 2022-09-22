# 프리셀
import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t + 1):
    # memory = 기억하는 플레이한 게임 수
    # winrate_today = 오늘 승률
    # winrate_total = 누적 승률
    memory, winrate_today, winrate_total = map(int, input().split())
    answer = 'Possible'
    win_today = int(winrate_today * memory / 100)
    lose_today = memory - win_today
    if winrate_total == 100 and lose_today > 0 or winrate_total == 0 and winrate_today > 1:
        answer = 'Broken'
    print(f'#{tc} {answer}')

