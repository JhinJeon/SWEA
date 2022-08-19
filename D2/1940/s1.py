# 가랏! RC카!

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    times = []
    cmds = []
    velocity = 0
    distance = 0
    for i in range(n):
        cmd = list(map(int, input().split()))
        if cmd[0] == 2:
            velocity -= cmd[1]
            if velocity < 0:
                velocity = 0
        elif cmd[0] == 1:
            velocity += cmd[1]
        distance += velocity

    print(f'#{tc} {distance}')
