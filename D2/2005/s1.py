# 최초로 작성한 코드(구글링 참고)

tc = int(input())

for t in range(1, tc+1):
    result = []
    n = int(input())
    for i in range(n):
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(result[i-1][j] + result[i-1][j-1])
        result.append(temp)

    print(f'#{tc}')
    for i in result:
        print(*i)
