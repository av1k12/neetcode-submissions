class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        count = 0
        def dfs(node: int) -> None:
            if node in visited:
                return
            visited.add(node)

            for neighbor in adj[node]:
                dfs(neighbor)

        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)
                
        return count