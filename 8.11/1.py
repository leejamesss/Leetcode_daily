from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 构建邻接表，key为起点，value为终点列表
        graph = defaultdict(list)
        for ticket in tickets:
            from_city, to_city = ticket
            graph[from_city].append(to_city)
        
        # 按字典序对终点列表进行排序
        for city in graph:
            graph[city].sort()
        
        # 使用DFS遍历每一个节点，并将其加入结果列表中
        itinerary = []
        def dfs(city):
            while graph[city]:
                next_city = graph[city].pop(0)
                dfs(next_city)
            itinerary.insert(0, city)
        
        dfs('JFK')
        return itinerary
# https://leetcode.cn/problems/reconstruct-itinerary/
