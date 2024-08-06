def solveNQueens(n):
    def dfs(row, cols, diags1, diags2):
        if row == n:
            return 1
        count = 0
        available_positions = (~(cols | diags1 | diags2)) & ((1 << n) - 1)
        while available_positions:
            position = available_positions & -available_positions
            available_positions &= available_positions - 1
            count += dfs(row + 1, cols | position, (diags1 | position) << 1, (diags2 | position) >> 1)
        return count
    
    return dfs(0, 0, 0, 0)

def solution(n):
    return solveNQueens(n)