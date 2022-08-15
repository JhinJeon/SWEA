# 달팽이 숫자
# while을 사용하지 않고 풀기

t = int(input())

# dx, dy = 그래프에서 이동하는 값(우, 하, 좌, 상 순)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for tc in range(1, t+1):
    n = int(input())

    # graph = n*n의 이차원 리스트
    # direction = 진행 방향(기본 : 오른쪽)
    # x, y = 그래프 상 좌표(x는 열, y는 행)
    # val = 배열 안에 넣을 값
    graph = [[0] * n for _ in range(n)]
    direction = 0
    x = 0
    y = 0

    # val = graph 안에 채울 값
    for val in range(1, n**2+1):
        graph[y][x] = val
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 이동한 위치가 그래프를 벗어나지 않으면서 값이 0인 경우 원래 방향으로 좌표 이동
        if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 0:
            x = nx
            y = ny

        # 그렇지 않은 경우 회전 후 회전한 방향으로 좌표 이동
        else:
            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]

    # 테스트 케이스 번호와 그래프를 차례대로 출력
    print(f'#{tc}')
    for col in graph:
        print(*col)
