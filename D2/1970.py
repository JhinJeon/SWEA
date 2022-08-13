# 쉬운 거스름돈

t = int(input())

# changes = 거스름돈 단위 리스트
changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, t+1):
    # money = 거슬러 줘야 할 돈
    money = int(input())
    # change_result = 거스름돈으로 주는 돈의 개수 카운트
    change_result = [0] * 8

    # changes의 거스름돈 단위로 거슬러 줄 수 있으면 money에서 거스름돈 금액을 차감
    # 이후 change_result에 거스름돈 개수 +1
    for i in range(len(changes)):
        while money // changes[i] > 0:
            money -= changes[i]
            change_result[i] += 1

    # 결과 출력(리스트 언패킹)
    print(f'#{tc}')
    print(*change_result)
