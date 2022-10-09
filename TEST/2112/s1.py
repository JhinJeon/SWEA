# 보호필름
import sys
sys.stdin = open('sample_input.txt')


# 각 단면의 세로 방향 테스트
def filmtest(row_id):
    stack = 1
    for col in range(1, density):
        if film[col-1][row_id] == film[col][row_id]:
            stack += 1
        else:
            stack = 1
        if stack == standard:
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
        if not filmtest(w):
            break
    else:
        if changecount != 1:
            answer = changecount
        return

    for idx in range(density):
        if not changed[idx]:
            changed[idx] = True
            film_a = film_info.copy()
            film_a[idx] = [0] * width
            differaction(film_a, idx, changecount + 1)

            film_b = film.copy()
            film_b[idx] = [1] * width
            differaction(film_b, idx, changecount + 1)

            changed[idx] = False


t = int(input())

for tc in range(1,t+1):
    density, width, standard = map(int,input().split())     # density = 두께, width = 가로 너비, standard = 합격 기준

    film = [list(map(int,input().split())) for _ in range(density)]
    answer = density

    changed = [False] * density

    differaction(film, 0, 0)
    print(f'#{tc}', answer)