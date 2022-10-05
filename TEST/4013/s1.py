# 특이한 자석
from collections import deque
import sys

sys.stdin = open('sample_input.txt')


# 기준 idx 값 중심으로 turn 방향을 계산하는 함수
def def_turn(idx):
    left = idx - 1
    right = idx + 1
    if left >= 0 and magnetic_info[left][2] != magnetic_info[idx][6] and not turn[left]:
        turn[left] = turn[idx] * -1
        def_turn(left)
    if right < 4 and magnetic_info[right][6] != magnetic_info[idx][2] and not turn[right]:
        turn[right] = turn[idx] * -1
        def_turn(right)
    # 양 쪽으로 탐색할 기회가 없는 경우 return
    return

# 자석 정보는 12시 부터 시계 방향으로 제공
# 2번과 6번 인덱스 기준
# n극 = 0, s극 = 1
# s극 ** 인덱스 번호의 합계

t = int(input())

for tc in range(1,t+1):
    rotate_count = int(input())
    magnetic_info = []
    
    # 자석 정보 입력
    for _ in range(4):
        magnetic_info.append(deque(map(int, input().split())))

    # [회전할 자석 번호, 회전 방향] 저장
    rotation_input = [list(map(int, input().split())) for _ in range(rotate_count)]

    for rotate in rotation_input:
        turn = [0] * 4  # 회전 방향(0 = 변화 없음)
        std = rotate[0] - 1     # 회전할 자석(인덱스 범위 보정)
        turn[std] = rotate[1]

        # 회전한 자석의 왼쪽/오른쪽부터 순차적으로 수정

        def_turn(std)

        for i in range(4):
            # 시계 방향 회전인 경우
            if turn[i] == 1:
                pop_value = magnetic_info[i].pop()
                magnetic_info[i].appendleft(pop_value)
            # 시계 반대 방향 회전인 경우
            elif turn[i] == -1:
                magnetic_info[i].append(magnetic_info[i].popleft())

    # 점수 정산
    answer = 0
    for m in range(4):
        if magnetic_info[m][0] == 1:
            answer += 2 ** m

    print(f'#{tc}', answer)