# 서랍의 비밀번호
p, k = map(int,input().split())
try_count = 1
for i in range(1000):
    if p == k:  # 비밀번호가 일치하는 경우
        break
    try_count += 1
    k += 1
    if k > 999: # 마지막으로 시도해 본 번호가 999인 경우 0으로 리셋
        k = 0
print(try_count)