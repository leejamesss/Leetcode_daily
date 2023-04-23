# https://leetcode.cn/problems/word-search/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, cur_word):
            # 边界条件
            if row < 0 or row >= m or col < 0 or col >= n or visited[row][col] or board[row][col] != cur_word[0]:
                return False
            # 触发条件
            if len(cur_word) == 1:
                return True
            visited[row][col] = True
            for i, j in [(row-1,col), (row+1,col), (row,col-1), (row,col+1)]:
                if dfs(i, j, cur_word[1:]):
                    return True
            visited[row][col] = False
            return False
        
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if dfs(i, j, word):
                    return True
        return False

