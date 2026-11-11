class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build the adjacency list mapping course -> list of prerequisites
        # adj[course] = [prereq1, prereq2, ...]
        adj = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        # States for 3-color cycle detection:
        # 0 = UNVISITED (not yet processed)
        # 1 = VISITING  (currently on the active recursion call stack)
        # 2 = VISITED   (completely explored, confirmed cycle-free)
        state = [0] * numCourses
        def has_cycle(crs: int) -> bool:
            if state[crs] == 1:
                return True

            if state[crs] == 2:
                return False
            
            state[crs] = 1 #mark as visiting (currently on recursion track)

            for pre in adj[crs]: #check each prereq
                if has_cycle(pre):
                    return True
            state[crs] = 2
            return False
        for crs in range(numCourses):
            if state[crs] == 0:
                if has_cycle(crs):
                    return False
        return True
