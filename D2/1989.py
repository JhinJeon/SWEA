# 초심자의 회문 검사

T = int(input())
for tc in range(1, T + 1):
    txt = input()
    # 문자열 길이가 1인 경우
    if len(txt) == 1:
        print(f"#{tc} 1")
    # 문자열 길이가 2 이상인 경우 문자열의 가장자리부터 양 쪽이 같은지 비교
    for j in range(len(txt) // 2):
        # 양쪽이 다른 경우 회문 아님(0) 출력
        if txt[j] != txt[-1 - j]:
            print(f"#{tc} 0")
            break
        # 양쪽이 모두 같은 경우 회문임(1) 출력
    else:
        print(f"#{tc} 1")
