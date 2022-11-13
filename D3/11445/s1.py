# 무한 사전

t = int(input())

for tc in range(1, t+1):
    answer = 'N'            # 중간 단어 유무 판별(기본: 없음)
    case1 = str(input().strip())     # 첫 번째 단어
    case2 = str(input().strip())     # 두 번째 단어

    if case1 + 'a' != case2:
        answer = 'Y'

    print(f'#{tc} {answer}')
