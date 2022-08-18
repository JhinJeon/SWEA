# 최빈수 구하기

t = int(input())

for k in range(1, t+1):
    n = int(input())
    # scores = 점수 목록
    # score_count = 점수 집계(값 = 점수가 나온 횟수)
    scores = list(map(int, input().split()))
    score_count = [0] * 101
    for s in scores:
        score_count[s] += 1

    # most_frequent = 가장 빈번하게 나온 횟수
    most_frequent = 0
    answer = 0
    for idx, sc in enumerate(score_count):
        if sc >= most_frequent:
            most_frequent = sc
            answer = idx

    # answer_max = 가장 자주 나온 점수
    print(f'#{k} {answer}')
