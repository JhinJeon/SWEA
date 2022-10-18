# 알파벳 공부

standard = 'abcdefghijklmnopqrstuvwxyz'

t = int(input())

for tc in range(1, t+1):
    study = input()

    correct = 0
    for spell in range(len(study)):
        if study[spell] != standard[spell]:
            break
        correct += 1

    print(f'#{tc}', correct)
