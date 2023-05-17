
# https://leetcode.cn/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
```python
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF=1000000
        adj = [ [INF for _ in range(n) ] for i in range(n)]
        for _ in range(n):
            adj[_][_]=0

        for edge in edges:
            k,w = edge[1],edge[2]
            num=edge[0]
            adj[num][k] =w
            adj[k][num] =w
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    adj[j][k] =min(adj[j][k],adj[j][i]+adj[i][k])
        sum_lst=[]
        for id in range(n):
            lst=adj[id]
            sum=0
            for k in lst:
                if k <=distanceThreshold and k!=0:
                    sum+=1
            sum_lst.append(sum)

        least=min(sum_lst)
        id_lst=[]
        for i in range(n):
            if sum_lst[i] ==least:
                id_lst.append(i)
                
        return max(id_lst)
```
