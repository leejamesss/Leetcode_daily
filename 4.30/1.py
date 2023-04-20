#https://leetcode.cn/problems/number-of-provinces/submissions/
class Solution:
    def dfs(self, isConnected: List[List[int]], visited: List[int], i: int, memo: Dict[Tuple[int, int], bool]) -> bool:
        if (i, visited[i]) in memo:
            return memo[(i, visited[i])]
        # 标记节点 i 为已访问
        visited[i] = True
        # 遍历节点 i 的所有相邻节点
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and not visited[j]:
                self.dfs(isConnected, visited, j, memo)
        memo[(i, visited[i])] = True
        return True
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = [False] * len(isConnected)
        memo = {}
        for i in range(len(visited)):
            # 如果节点 i 没有被访问过，说明它在一个新的连通分量中
            if not visited[i]:
                provinces += 1
                self.dfs(isConnected, visited, i, memo)
        return provinces

#思路是深搜，然后标记节点是否访问过，直到没得访问为止，这样可以找出一个子图，然后再在没有访问的节点中随便找个节点，然后继续访问，最后记录找出的连通子图的个数
#用记忆化搜索进行优化
