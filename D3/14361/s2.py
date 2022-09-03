# 숫자가 같은 배수
# SWEA 제출용(테스트 케이스 오류)

t = int(input())

for tc in range(1, t+1):
    number = int(input())
    value_check = str(number)
    answer = False
    for i in range(number * 2, number * 10, number):
        str_num = str(i)
        for s in str_num:
            if s not in value_check or len(str_num) != len(value_check):
                break
        else:
            answer = 'possible'
            break
    else:
        answer = 'impossible'

    print(f'#{tc}', answer)
