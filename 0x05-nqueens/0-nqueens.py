#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens
"""
import sys


def solveNQueens(N):
    """Solve N queens"""
    col = []
    post_diag = []
    neg_diag = []
    res = []

    def solve(row):
        """Solve"""
        if row == N:
            res.append([[i, col[i]] for i in range(N)])
            return
        for i in range(N):
            if (i not in col and row + i
                    not in post_diag and row - i not in neg_diag):
                col.append(i)
                post_diag.append(row + i)
                neg_diag.append(row - i)
                solve(row + 1)
                col.pop()
                post_diag.pop()
                neg_diag.pop()

    solve(0)
    return res


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    N = int(sys.argv[1])

    res = solveNQueens(N)
    for i in res:
        print(i)
