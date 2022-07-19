# 중간값 찾기
n = int(input())
finder = int((n-1)/2)
score = list(map(int,input().strip().split()))
score.sort()	#sort는 기본적으로 오름차순으로 정렬
print(score[finder])