t = int(input())

for k in range(1, t + 1):
    n, student_id = map(int, input().split())
    # total = 학생 성적 저장용 리스트
    total = []
    score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    # 학생별 원점수 계산
    for i in range(n):
        mid_term, final_term, report = map(int, input().split())
        total.append(mid_term * 0.35 + final_term * 0.45 + report * 0.2)
    # 학생 순위 계산
    student_rank = n
    for point in total:
        if total[student_id - 1] > point:
            student_rank -= 1
    # 학점으로 전환(상대비율 고려)
    score_rank = student_rank * 10 // n
    if (student_rank * 10) % n == 0:
        score_rank -= 1
    print(f'#{k} {score[int(score_rank)]}')
