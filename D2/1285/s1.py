# 아름이의 돌 던지기
# C++ 전용 문제라 제출은 불가능

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    records = list(map(int, input().split()))
    max_record = 100000
    for r in records:
        r = abs(r)
        if r < max_record:
            max_record = r

    even_count = records.count(max_record)
    print(f'#{tc}', max_record, even_count)
