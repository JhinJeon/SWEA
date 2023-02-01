# RGB 거리

# n = 전체 집 개수
n = int(input())

# palette = 색상별 비용 정보 저장용 리스트
palette = []

answer = 0      # 누적 합계
selected = -1    # 직전에 선택한 색상(인덱스 번호)

# 기본 정보 입력
for i in range(n):
    palette.append(list(map(int, input().split())))
    
# 각 팔레트 구역을 해당 색상을 칠하는 데 필요한 누적 최소 비용으로 대체
for k in range(n-1):
    palette[k+1][0] += min(palette[k][1], palette[k][2])
    palette[k+1][1] += min(palette[k][0], palette[k][2])
    palette[k+1][2] += min(palette[k][0], palette[k][1])

# 결과 출력
answer = min(palette[-1])
print(answer)
