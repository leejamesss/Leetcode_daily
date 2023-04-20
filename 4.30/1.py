#https://leetcode.cn/problems/number-of-provinces/submissions/
class Solution:
    def dfs(self, isConnected: List[List[int]], visited: List[int], i: int):
        visited[i] = 1
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and not visited[j]:
                self.dfs(isConnected, visited, j)
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = [0] * len(isConnected)
        for i in range(len(visited)):
            if not visited[i]:
                provinces += 1
                self.dfs(isConnected, visited, i)
        return provinces
