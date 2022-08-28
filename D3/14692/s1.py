# 통나무 자르기
import sys
sys.stdin = open('sample_input.txt')


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    turn = 0
    if n % 2 != 0:
        answer = 'Bob'
    else:
        answer = 'Alice'
    print(f'#{tc} {answer}')