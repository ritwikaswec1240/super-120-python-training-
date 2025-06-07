# =========================== Print Adjacency List ===========================

from typing import List

class Solution:
    def printGraph(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        adjList = []
        for i in range(V):
            adjList.append([])
        for n, m in edges:
            adjList[n].append(m)
            adjList[m].append(n)
        for lst in adjList:
            lst.sort()
        return adjList


# =========================== BFS of Graph ===========================

class Solution:
    def bfs(self, adj: List[List[int]]) -> List[int]:
        v = len(adj)
        visited = [0] * v
        startNode = 0
        ans = []
        q = []

        if visited[startNode] == 0:
            visited[startNode] = 1
            q.append(startNode)
            while q:
                node = q.pop(0)
                ans.append(node)
                for i in adj[node]:
                    if visited[i] == 0:
                        visited[i] = 1
                        q.append(i)
        return ans


# =========================== DFS of Graph (Iterative) ===========================

class Solution:
    def dfs(self, adj: List[List[int]]) -> List[int]:
        v = len(adj)
        visited = [0] * v
        ans = []
        stack = []

        startNode = 0
        stack.append(startNode)

        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = 1
                ans.append(node)
                # Reverse to maintain similar order as recursive DFS
                for neighbor in reversed(adj[node]):
                    if not visited[neighbor]:
                        stack.append(neighbor)

        return ans
