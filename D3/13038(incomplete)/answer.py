# 교환학생

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    a = list(map(int, input().split()))
    answer = 0

    class_of_week = sum(a)
    remainder = n % class_of_week if n % class_of_week else class_of_week
    answer += (n - remainder) // class_of_week * 7
    minimum = 7
    for i in range(7):
        min_cnt = 0
        cnt = 0
        j = i
        while True:
            cnt += a[j]
            min_cnt += 1
            if cnt == remainder:
                break
            j = (j + 1) % 7
        if minimum > min_cnt:
            minimum = min_cnt
    answer += minimum
    print(f"#{tc} {answer}")
