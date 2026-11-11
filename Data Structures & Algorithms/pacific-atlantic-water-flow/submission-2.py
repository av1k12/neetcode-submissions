class Solution:
    #start at border edges and see where water flows uphill
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pac_reachable = set()
        atl_reachable = set()

        def dfs(r: int, c: int, reachable: set) -> None:
            reachable.add((r, c))

            for dr, dc in [(1,0), (-1, 0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr,nc) not in reachable and heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, reachable)

        #pacific side
        for c in range(cols):
            dfs(0, c, pac_reachable)
        for r in range(rows):
            dfs(r, 0, pac_reachable)

        #atl side
        for c in range(cols):
            dfs(rows-1, c, atl_reachable)
        for r in range(rows):
            dfs(r, cols - 1, atl_reachable)

        return[[r,c] for r, c in pac_reachable & atl_reachable]