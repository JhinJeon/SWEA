# 패턴 마디의 길이

t = int(input())
for k in range(1, t+1):
    txt = list(input())
    answer = []
    for i in range(1, len(txt)):
        rept = txt[:i]
        if rept * (len(txt)//i) + txt[:(len(txt) % i)] == txt:
            answer.append(i)
    print('#'+str(k), str(min(answer)))
