from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 建立邻接表
        graph = [[] for _ in range(numCourses)]
        # 统计每个课程的入度数
        in_degree = [0] * numCourses
        for cur, pre in prerequisites:
            graph[pre].append(cur)
            in_degree[cur] += 1
        
        # BFS
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        res = []
        
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(res) != numCourses:
            return []
        else:
            return res
# https://leetcode.cn/problems/course-schedule-ii/submissions/
