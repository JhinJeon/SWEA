# 숫자 조작

t = int(input())

for tc in range(1, t+1):
    input_data = input()
    num = list(input_data)
    min_value = int(input_data)
    max_value = int(input_data)

    for i in range(len(num)):
        for j in range(i+1, len(num)):
            num[j], num[i] = num[i], num[j]
            new_num = ''
            for n in num:
                new_num += n
            if new_num[0] != '0':
                new_num = int(new_num)
                if new_num < min_value:
                    min_value = new_num
                if new_num > max_value:
                    max_value = new_num
            num[j], num[i] = num[i], num[j]

    print(f'#{tc}', min_value, max_value)
