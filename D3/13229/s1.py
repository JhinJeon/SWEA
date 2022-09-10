# 일요일

weekday = {
    'SAT': 1,
    'FRI': 2,
    'THU': 3,
    'WED': 4,
    'TUE': 5,
    'MON': 6,
    'SUN': 7
}

t = int(input())

for tc in range(1,t+1):
    key = input()
    answer = weekday.get(key)
    print(f'#{tc}', answer)