# 무선 충전

# 순서대로 이동 안 함, 상, 우, 하, 좌
import sys
sys.stdin = open('sample_input.txt')

dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]

t = int(input())

for tc in range(1, t+1):
    m, a = map(int, input().split())    # m = 이동 횟수, a = 충전기의 개수
    user_1 = list(map(int, input().split()))    # user 1의 이동 패턴
    user_2 = list(map(int, input().split()))

    charger_array = [[] for _ in range(a)]      # 충전 가능 범위
    charger_power = [[] for _ in range(a)]      # 충전량

    # 충전기 별 사용 가능 범위 기록
    for case in range(a):
        # x, y = 중심점, arr = 반경, pw = 충전량
        x, y, arr, pw = map(int, input().split())
        charger_power[case] = pw  # 충전기 성능 추가

        # 충전 가능 범위 추가
        additional_array = list()
        for row in range(x-arr-1, x+arr):
            if 0 <= row < 10:
                for col in range(y-arr-1, y+arr):
                    if 0 <= col < 10:
                        if abs(row - x) + abs(col - y) <= arr - 1:
                            additional_array.append((row, col))

        charger_array[case].extend(list(additional_array))

    # user 1의 시작 위치
    u1_x = 0
    u1_y = 0
    # user 2의 시작 위치
    u2_x = 9
    u2_y = 9

    u1_using = -1   # 어떤 충전기 사용 중인지 확인(-1 : 충전기 미사용)
    u2_using = -1   # 어떤 충전기 사용 중인지 확인(-1 : 충전기 미사용)

    answer = 0  # 모든 사용자의 충전량
    # 사용자의 이동 기록 대조
    for idx in range(m):
        dir_u1 = user_1[idx]    # user 1의 다음 이동 방향
        dir_u2 = user_2[idx]    # user 2의 다음 이동 방향

        u1_x = u1_x + dx[dir_u1]
        u1_y = u1_y + dy[dir_u1]
        u2_x = u2_x + dx[dir_u2]
        u2_y = u2_y + dy[dir_u2]

        charger_use_u1 = []     # 사용자 1이 이용할 충전소 목록
        charger_use_u2 = []     # 사용자 2가 이용할 충전소 목록
        # 각 사용자별로 이용 가능한 충전량 가져오기
        for charger_no in range(a):
            if (u1_x, u1_y) in charger_array[charger_no]:
                charger_use_u1.append(charger_power[charger_no])
            if (u2_x, u2_y) in charger_array[charger_no]:
                charger_use_u2.append(charger_power[charger_no])

        energy = 0  # answer에 합산할 충전량
        # 둘 다 사용 가능한 충전소가 없는 경우
        if not charger_use_u1 and not charger_use_u2:
            energy = 0
            
        # 사용자 1만 사용 가능한 경우
        elif not charger_use_u2:
            energy = max(charger_use_u1)
            
        # 사용자 2만 사용 가능한 경우
        elif not charger_use_u1:
            energy = max(charger_use_u2)
        
        # 둘 다 사용 가능한 경우
        else:
            energy = 0
            for case1 in charger_use_u1:
                for case2 in charger_use_u2:
                    if case1 == case2 and energy < case1:
                        energy = case1
                    else:
                        if case1 + case2 > energy:
                            case_sum = case1 + case2
                            
        # 중간 결과 합산
        answer += energy
        
    print(f'#{tc}', answer)


# 0| 0 1 * 3 4
# 1| 0 * * * 4
# 2| * * * * *   22 // 12 21 32 23 // 20 31 42 33 24 13 02
# 3| 0 * * * 4
# 4| 0 1 * 3 4
