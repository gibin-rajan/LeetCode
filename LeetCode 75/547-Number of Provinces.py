class Solution:
    def findCircleNum(self, isConnected):
        N = len(isConnected)
        adjList = defaultdict(list)
        for row in range(N):
            for col in range(row + 1, N):
                if isConnected[row][col] == 1:
                    adjList[row + 1].append(col + 1)
                    adjList[col + 1].append(row + 1)
        
        def dfs(city):
            if city in visited:
                return False

            visited.add(city)
            neighbours = adjList[city]
            for neigh in neighbours:
                dfs(neigh)
            return True
        
        visited = set()
        provinces = 0
        for city in range(1, N + 1):
            if city not in visited and dfs(city):
                provinces += 1
        
        return provinces
    # Time: O(n^2) where n is the number of cities. dfs is called n times, and each time it takes O(n) for scanning the neighbours
    # Space: O(n) it's the space needed by the set visited, the adjList and the call stack for the dfs function
