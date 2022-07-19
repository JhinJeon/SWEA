# N줄 덧셈

# VSC에서는 맞는데 SW Expert Academy에서는 틀리는 코드

n = int(input())

def total(num):
    if num == 1:
        return 1
    else:
        return num + total(num-1)

print(total(n))

# SW Academy에서 이 코드를 돌리면 답이 351이 나오는데 결과는 Pass가 되는 현상이 있음