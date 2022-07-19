# 1대1 가위바위보
a,b = input().split()
a = int(a)
b = int(b)
if a == (b % 3) + 1:
    print('A')
if b == (a % 3) + 1:
    print('B')