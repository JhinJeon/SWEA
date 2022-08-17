# 파스칼의 삼각형
# 재귀함수로 구현

def pascal_triangle(col, row):
    if col == 0 or row == 0 or col == row:
        return 1
    else:
        return pascal_triangle(col-1, row) + pascal_triangle(col-1, row-1)


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    result = []
    print(f'#{tc}')

    for i in range(n):
        triangle_col = []
        for j in range(i+1):
            triangle_col.append(pascal_triangle(i, j))
        print(*triangle_col)
