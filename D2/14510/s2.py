# 일부 테스트케이스에서 날짜 배분 최적화가 안 되는 문제 발생

import sys
# sys.stdin = open('Sample_input.txt')
sys.stdin = open('debug.txt')

t = int(input())

for tc in range(1, t+1):
    n = int(input())    # 나무 개수
    trees = list(map(int, input().split()))      # 나무 상태

    max_height = max(trees)     # 나무의 최대 길이(성장 목표)
    odd = 0     # 물을 1 더 줘야 하는 나무의 수
    even = 0    # 물을 2 더 줘야 하는 나무의 수

    answer = 0      # 총 소요 기간

    # 1. 나무 별 추가로 줘야 하는 물의 양 계산

    for t in trees:
        gap = max_height - t

        # 물을 3 이상 주어야 하는 경우 미리 계산(홀수일 + 짝수일)
        while gap - 3 >= 0:
            gap -= 3
            answer += 2

        # 1만큼 남은 경우 odd + 1
        if gap == 1:
            odd += 1

        # 2만큼 남은 경우 even + 1
        elif gap == 2:
            even += 1

    # 2. 1 또는 2만 더 주면 되는 경우 계산

    while even:
        # odd 또는 even이 0이 될 때까지 반복
        while odd and even:
            odd -= 1
            even -= 1
            answer += 2

        # 짝수 1개만 남은 경우 break
        if odd <= 0 and even <= 1:
            break

        # 짝수만 남은 경우 2를 1 두개로 분해
        if even - odd > 1:
            even -= 1
            odd += 2

    # 홀수만 남은 경우(물이 모자란 나무마다 1씩만 주면 되는 경우)
    if odd:
        answer += 2 * odd - 1

    # 짝수가 남은 경우(+2만 1번 더 주면 되는 경우)
    elif even:
        answer += 2

    print(f'#{tc}', answer)


# 보충 - 알고리즘 도출 과정

# 1개면 +2 1회
# 2
# 0 - 2

# 2개면 +1 2회, +2 1회
# 2 /  2
# (1, 1) / 2
# 1 - 2 - 1

# 3개면 +1 2회, +2 2회
# (1, 1) / 2 / 2
# 1- 2 - 1 - 2

# 4개면 +1 2회, +2 3회
# 2 / 2 / 2 / 2
# (1, 1) / 2 / 2 / 2
# 1 - 2 - 1 - 2 - 0 - 2

# 5개면 +1 4회, +1 3회
# 2 / 2 / 2 / 2 / 2
# (1, 1) / 2 / (1, 1) / 2 / 2
# 1 - 2 - 1 - 2 - 1 - 2 - 1

# 6개면 +1 4회, +2 4회
# (1, 1) / 2 / (1, 1) / 2 / 2 / 2
# 1 - 2 - 1 - 2 - 1 - 2 - 1 - 2


# 7개면 +1 4회, +2 5회
# 2 / 2 / 2 / 2 / 2 / 2 / 2
# (1, 1) / 2 / (1, 1) / 2 / 2 / 2 / 2
# 1 - 2 - 1 - 2 - 1 - 2 - 1 - 2 - 0 - 2
