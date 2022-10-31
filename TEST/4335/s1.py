# 무인도 탈출
# 시간 단축 요소 필요
import sys
sys.stdin = open('sample_sample_input.txt')
# sys.stdin = open('debug.txt')


# 밑바닥에 까는 상자별로 도출 가능한 최대 높이 반환
def box_dfs(x, y, z):  # 가로, 세로, 누적 높이
    global answer, box_used

    for k in range(n):
        if not box_used[k]:
            a, b, c = boxes[k]
            if a <= x and b <= y or a <= y and b <= x:
                box_used[k] = True
                box_dfs(a, b, z + c)
                box_used[k] = False
            if a <= x and c <= y or c <= x and a <= y:
                box_used[k] = True
                box_dfs(a, c, z + b)
                box_used[k] = False
            if b <= x and c <= y or b <= y and c <= x:
                box_used[k] = True
                box_dfs(b, c, z + a)
                box_used[k] = False

    # 모든 상자를 사용한 경우
    if z > answer:
        answer = z


t = int(input())

for tc in range(1, t + 1):
    n = int(input())  # 상자 개수
    boxes = []
    for i in range(n):
        boxes.append(list(map(int, input().split())))

    box_used = [False] * n  # 상자 사용 여부
    answer = 0

    box_dfs(10000, 10000, 0)
    print(f'#{tc}', answer)
