# 점심 식사시간

t = int(input())

for tc in range(1, t+1):
    n = int(input())

    # 1번 계단 입력 여부
    stair1 = False

    # 사람 위치
    people = []

    # 지도 정보
    graph = [list(map(int,input().split())) for _ in range(n)]

    # 계단 좌표와 사람 좌표 추가
    for col in range(n):
        for row in range(n):
            if graph[col][row] == 1:
                people.append((row, col))
            elif graph[col][row] > 1:
                # 1번 계단 정보가 있으면 2번 계단 좌표 기억
                if stair1:
                    s2_x, s2_y = row, col
                # 1번 계단 정보가 없으면 1번 계단 좌표 기억 후 입력 여부 체크
                else:
                    s1_x, s1_y = row, col
                    stair1 = True

    # 사람 별 계단 이용에 몇 분이 걸리는지 확인
    stair_1 = []
    stair_2 = []
    # 계단 길이
    s1_len = graph[s1_y][s1_x]
    s2_len = graph[s2_y][s2_x]

    for i in range(len(people)):
        px, py = people[i]
        x = abs(px-s1_x)
        y = abs(py-s1_y)
        stair_1.append(x + y + s1_len)
        x = abs(px-s2_x)
        y = abs(py-s2_y)
        stair_2.append(x + y + s2_len)


    print(f'#{tc}')