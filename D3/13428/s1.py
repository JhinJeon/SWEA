# 숫자 조작

t = int(input())

for tc in range(1, t+1):
    input_data = input()
    num = list(input_data)
    min_value = int(input_data)
    max_value = int(input_data)

    for i in range(1, len(num)):
        if num[i] != '0':
            num[0], num[i] = num[i], num[0]
            new_num = ''
            for n in num:
                new_num += n
            new_num = int(new_num)
            if new_num < min_value:
                min_value = new_num
            if new_num > max_value:
                max_value = new_num
            num[0], num[i] = num[i], num[0]

    print(f'#{tc}', min_value, max_value)
