# 숫자를 정렬하자

T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    # nlist, mlist = 개별 숫자열 리스트
    # ansum = 마주보는 숫자들의 곱을 저장하는 리스트
    nlist = []
    mlist = []
    ansum = []
    nlist = list(map(int, input().split()))
    mlist = list(map(int, input().split()))

    # mlist가 더 긴 경우
    if n < m:
        for k in range(m-n+1):
            answer = []
            for i in range(len(nlist)):
                answer.append(nlist[i]*mlist[i+k])
            ansum.append(sum(answer))

    # nlist가 더 긴 경우
    elif n > m:
        for k in range(n-m+1):
            answer = []
            for i in range(len(mlist)):
                answer.append(nlist[i+k]*mlist[i])
            ansum.append(sum(answer))

    # 둘 다 동일한 길이인 경우
    else:
        answer = []
        for i in range(nlist):
            answer.append(nlist[i]*mlist[i])
        ansum.append(sum(answer))
    print('#'+str(t+1)+' '+str(max(ansum)))
