# 초심자의 회문 검사

T = int(input())
for i in range(1, T+1):
    txt = input()
    if len(txt) == 1:
        print("#"+str(i)+" "+'1')
    for j in range(len(txt)//2):
        if txt[j] != txt[-1-j]:
            print("#"+str(i)+" "+'0')
            break
        print("#"+str(i)+" "+'1')
        break
