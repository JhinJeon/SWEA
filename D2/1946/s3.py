# 간단한 압축 풀기

T = int(input())
for k in range(0, T):
    N = int(input())

    # text_words = 문자 a를 b개만큼 추가할 빈 문자열
    text_words = ''
    for i in range(N):
        a, b = input().split()
        b = int(b)

        # 변수 a에 저장된 문자를 b번 추가
        text_words += a * b
    print(f'#{k+1}')

    # 인덱스 번호 끝 자리가 9로 끝날 때마다 줄바꿈
    # idx > 0 조건은 맨 첫 번째 문자를 출력할 때 줄바꿈을 일으키지 않기 위함
    for idx, val in enumerate(text_words):
        if idx > 0 and idx % 10 == 9:
            print(val)
        else:
            print(val, end='')
    print()
