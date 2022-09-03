# 숫자가 같은 배수
# 정답(SWEA에서는 틀리다고 나옴)

t = int(input())

for tc in range(1, t+1):
    number = int(input())
    value_check = str(number)
    answer = False
    for i in range(number * 2, number * 10, number):
        str_num = str(i)
        for v in value_check:
            if v not in str_num or len(str_num) != len(value_check):
                break
        else:
            answer = 'possible'
            break
    else:
        answer = 'impossible'

    print(f'#{tc}', answer)
