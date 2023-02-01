# RGB 거리
# 그리디 방식으로 해결(오답)

# n = 전체 집 개수
n = int(input())

# palette = 색상별 비용 정보 저장용 리스트
palette = []

answer = 0      # 누적 합계
selected = -1    # 직전에 선택한 색상(인덱스 번호)

# 기본 정보 입력
for i in range(n):
    palette.append(list(map(int, input().split())))
    
# 각 팔레트마다 해당 팔레트에 도달할 수 있는 최소 비용으로 통일
for k in range(n-1):
    summary = 1000 * (k+2)   # 구역 별 최솟값을 계산하기 위한 임시 변수
    temp_selected = -1

    # 인접한 팔레트끼리 비교
    for idx1 in range(3):
        for idx2 in range(3):
            # 다른 색상의 조합끼리 비교
            if idx1 != idx2 and selected != idx2:
                temp = palette[k][idx1] + palette[k+1][idx2]

                # 최솟값을 경신하면 임시 변수 변경
                if temp < summary:
                    summary = temp
                    temp_selected = idx2


    # 계산 결과를 다음 팔레트에 덮어쓰기
    selected = temp_selected
    for j in range(3):
        palette[k+1][j] = summary

    print(palette[k+1])
    print(selected)
    print('-' * 20)

# 결과 출력
print(palette[n-1][0])