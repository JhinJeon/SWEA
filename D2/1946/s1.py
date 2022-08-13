# 간단한 압축 풀기

t = int(input())
for i in range(1, t+1):
    print(f"#{i}")
    n = int(input())
    # answer = 10개 단위로 끊어서 출력할 원본 문자열
    answer = ''
    # answer에 문자열 a를 b개만큼 추가
    for j in range(n):
        a, b = input().split()
        b = int(b)
        answer += a * b
    # 인덱스 번호가 0 또는 10의 배수인 경우 줄바꿈
    for i, char in enumerate(answer):
        if i > 0 and i % 10 == 0:
            print()
        print(char, end='')
    print()
