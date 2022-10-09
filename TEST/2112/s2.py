# 보호필름
import sys
sys.stdin = open('sample_input.txt')


# 각 단면의 세로 방향 테스트
def filmtest(test_film, row_id):
    stack = test_film[0][row_id]        # 직전 행의 값
    streak = 1      # 연속 등장 횟수
    for col in range(1, density):
        if test_film[col][row_id] == stack:
            streak += 1
        else:
            stack = (stack + 1) % 2
            streak = 1
        if streak == standard:
            break
    # 테스트 불합격
    else:
        return False
    # 테스트 합격(break에 걸린 경우)
    return True


# 각 단층의 속성 변경
def differaction(film_info, col_no, changecount):
    global answer, changed
    # 백트래킹
    if changecount >= answer:
        return
    # 성능 검사
    for w in range(width):
        if not filmtest(film_info, w):
            break
    else:
        answer = changecount
        return

    # 현재 행의 아래쪽 행부터 탐색(중복방지, 연산 최적화)
    for idx in range(col_no, density):
        if not changed[idx]:
            changed[idx] = True     # 탐색 여부 체크
            # film_a = 현재 슬라이드를 모두 0으로 전환
            film_a = film_info.copy()
            film_a[idx] = [0] * width
            if film_info[idx] != film_a[idx]:
                differaction(film_a, idx, changecount + 1)

            # film_b = 현재 슬라이드를 모두 1로 전환
            film_b = film_info.copy()
            film_b[idx] = [1] * width
            if film_info[idx] != film_b[idx]:
                differaction(film_b, idx, changecount + 1)

            changed[idx] = False        # 되돌리기


t = int(input())

for tc in range(1,t+1):
    density, width, standard = map(int,input().split())     # density = 두께, width = 가로 너비, standard = 합격 기준

    film = [list(map(int,input().split())) for _ in range(density)]
    answer = density

    changed = [False] * density

    differaction(film, 0, 0)

    print(f'#{tc}', answer)