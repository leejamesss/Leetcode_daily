class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses # 入度数组
        graph = [[] for _ in range(numCourses)] # 邻接表

        for cur, pre in prerequisites: # 构建入度数组和邻接表
            indegrees[cur] += 1
            graph[pre].append(cur)

        queue = collections.deque() # 初始化队列
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        while queue: # 拓扑排序
            cur = queue.popleft()
            numCourses -= 1
            for nxt in graph[cur]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    queue.append(nxt)

        return numCourses == 0
        
       # https://leetcode.cn/problems/course-schedule/submissions/
