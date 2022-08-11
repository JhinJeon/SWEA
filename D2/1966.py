# 숫자를 정렬하자

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    numlist = list(map(int, input().split()))
    for j in range(n):
        for i in range(j, n):
            if numlist[i] < numlist[j]:
                numlist[i], numlist[j] = numlist[j], numlist[i]

    print(f'#{tc}', *numlist)
