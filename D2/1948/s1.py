# 날짜 계산기
# datetime 함수 사용
from datetime import datetime

t = int(input())

for tc in range(1, t+1):
    m1, d1, m2, d2 = map(int, input().split())
    t1 = datetime.strptime(f"{m1}{d1}", '%m%d')
    t2 = datetime.strptime(f"{m2}{d2}", '%m%d')

    answer = t2 - t1
    print(f'#{tc} {answer.days+1}')
