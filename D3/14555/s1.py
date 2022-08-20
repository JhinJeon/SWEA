# 공과 잡초

t = int(input())

for tc in range(1, t+1):
    ground = input()
    ball_count = 0  # 공의 개수 저장
    ball_stack = []  # 공의 왼쪽 모양이 나온 경우 기록

    for g in ground:
        if g == '(':    # 공의 왼쪽만 보이는 경우
            ball_stack.append(g)
            ball_count += 1
        elif g == ')':
            if ball_stack:  # 하나의 공이 온전하게 보이는 경우
                ball_stack.pop()
            else:   # 공의 오른쪽만 보이는 경우
                ball_count += 1

        else:   # 잡초나 그냥 땅인 경우
            if ball_stack:  # 공의 왼쪽만 보이는 경우 ball_stack 초기화
                ball_stack.pop()

    print(f'#{tc} {ball_count}')
