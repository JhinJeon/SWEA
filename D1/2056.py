# 연월일 달력
t = int(input())
for k in range(1,t+1):
    input_date = str(input())
    answer = ''
    # month가 1~12 범위를 벗어나는 경우
    if int(input_date[4:6]) < 1 or int(input_date[4:6]) > 12:
        print('#'+str(k),-1)
        continue
    # 2월의 경우
    elif int(input_date[4:6]) == 2:
        day28 = list(range(1,29))
        if int(input_date[6:8]) in day28:
            answer = 'correct'
    else:
        month1 = [1,3,5,7,8,10,12]
        month2 = [4,6,9,11]
        day31 = list(range(1,32))
        day30 = list(range(1,31))
        # 1,3,5,7,8,10,12월의 경우
        if int(input_date[4:6]) in month1 and int(input_date[6:8]) in day31:
            answer = 'correct'
        elif int(input_date[4:6]) in month2 and int(input_date[6:8]) in day30:
            answer = 'correct'
    if answer == 'correct':
        print('#'+str(k),input_date[0:4]+'/'+input_date[4:6]+'/'+input_date[6:8])
    else:
        print('#'+str(k),-1)