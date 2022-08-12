#  어디에 단어가 들어갈 수 있을까

import sys
sys.stdin = open('input.txt')


def streak_check(graph, width, key):
    result = 0
    for col in range(width):
        streak_col = 0
        streak_row = 0
        for row in range(width):
            if graph[col][row] == 1:
                streak_row += 1
            else:
                if streak_row == key:
                    result += 1
            if graph[row][col] == 1:
                streak_col += 1
            else:
                if streak_col == key:
                    result += 1
        if streak_row == key or streak_col == key:
            result += 1
    return result


T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    puzzle = []
    for i in range(n):
        puzzle.append(list(map(int, input().split())))

    answer = streak_check(puzzle,n,k)

    print(f"#{test_case} {answer}")


