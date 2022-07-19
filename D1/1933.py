# 간단한 약수

n = int(input())
answer = []
for divider in range(1,n):
    if n % divider == 0:
        answer.append(divider)
answer.append(n)

for i in answer:
    print(i, end=' ')