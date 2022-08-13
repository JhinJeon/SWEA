# 간단한 압축 풀기

T = int(input())
for k in range(0, T):
    N = int(input())

    # textlist = 입력받은 문자열 종류 저장용 리스트
    textlist = []

    # 문자열 a를 b개만큼 추가
    for i in range(N):
        a, b = input().split()
        b = int(b)
        # textlist에는 a를 b번 추가
        for j in range(b):
            textlist.append(a)
    print('#'+str(k+1))
    # 10개 단위로 끊어서 출력
    for i in range(0, len(textlist)+1, 10):
        print(''.join(textlist[i:i+10]))
