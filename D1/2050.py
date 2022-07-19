# 알파벳을 숫자로 전환
alphabet = ['A','B','C','D','E','F','G',
            'H','I','J','K','L','M','N',
            'O','P','Q','R','S','T','U',
            'V','W','X','Y','Z']
alphabet_no = []
n = str(input())
for k in n:
    alphabet_no.append(str(alphabet.index(k)+1))
print(' '.join(alphabet_no))