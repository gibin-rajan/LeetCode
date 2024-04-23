class Solution:
    def calcEquation(self, equations, values, queries):
        graph = collections.defaultdict(list)
        
        for i in range(len(equations)):
            x,y = equations[i]
            graph[x].append([y,values[i]])
            graph[y].append([x,1/values[i]])
   
        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1
            queue = collections.deque()
            queue.append((src,1))
            seen = set()
            while queue:
                source, srcDenom = queue.popleft()
                if source == dst:
                    return 1/srcDenom
                seen.add(source)
                for destination, destDenom in graph[source]:
                    if destination not in seen:
                        queue.append((destination,srcDenom/destDenom))
            return -1
        
        result = []
        for u,v in queries:
            result.append(bfs(u,v))
        return result