# 치킨 배달
import sys
sys.stdin = open('sample1.txt')

from itertools import combinations

n, store_min = map(int, input().split())    # 집의 수(최대 2n개), 최소 상점 개수(최대 = 13)

graph = [list(map(int, input().split())) for _ in range(n)]

homes = []
stores = []
for col in range(n):
    for row in range(n):
        if graph[col][row] == 1:
            homes.append((row, col))
        elif graph[col][row] == 2:
            stores.append((row, col))

survived_stores = list(combinations(stores, store_min))

answer = 99999999
# 생존한 가게 경우의 수 탐색
for store in survived_stores:
    case_summary = 0
    # 집 좌표 하나씩 불러오기
    for hx, hy in homes:
        gap = []
        # 집에서 가장 가까운 가게 찾기
        for sx, sy in store:
            dx = abs(hx - sx)
            dy = abs(hy - sy)
            gap.append(dx + dy)
        # 집에서 가장 가까운 가게만 치킨 거리에 반영
        case_summary += min(gap)
        if case_summary > answer:
            break
    if case_summary < answer:
        answer = case_summary

print(answer)
