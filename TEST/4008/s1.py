# 숫자 만들기
import sys
sys.stdin = open('sample_input.txt')


def calculator(num_idx, value):
    global min_value, max_value
    if num_idx == n - 1:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
        return
    # 사칙연산 리스트에서 연산자 사용
    for idx in range(4):
        # 사용 가능한 연산자가 있는 경우
        if calculator_count[idx] > 0:
            # 연산자 개수 차감
            calculator_count[idx] -= 1
            # 덧셈인 경우
            if idx == 0:
                calculator(num_idx + 1, value + numbers[num_idx+1])
            # 뺄셈인 경우
            elif idx == 1:
                calculator(num_idx + 1, value - numbers[num_idx + 1])
            # 곱셈인 경우
            elif idx == 2:
                calculator(num_idx + 1, value * numbers[num_idx + 1])
            # 나눗셈인 경우
            else:
                if numbers[num_idx+1] != 0: # 0으로 나누기 방지
                    # 음수 나눗셈 처리
                    if value < 0:
                        next_value = (-value // numbers[num_idx + 1]) * -1
                    else:
                        next_value = value // numbers[num_idx + 1]
                    calculator(num_idx + 1, next_value)
            # 탐색 취소
            calculator_count[idx] += 1
    return


t = int(input())

for tc in range(1,t+1):
    n = int(input())
    calculator_count = list(map(int,input().split()))   # 순서대로 +, -, *, /의 개수
    numbers = list(map(int,input().split()))    # 숫자 목록
    min_value = 100000000
    max_value = -100000000
    start_value = numbers[0]

    calculator(0, start_value)

    answer = max_value - min_value
    print(f'#{tc}', answer)