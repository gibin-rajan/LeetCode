import heapq
class Solution:
    def totalCost(self, costs, k, candidates):
        n=len(costs)
        if candidates>n-candidates:
            costs.sort()
            return sum(costs[:k])
        st=[]
        end=[]        
        heapq.heapify(st)
        heapq.heapify(end)
        for i in range(candidates):
            heapq.heappush(st,costs[i])
            heapq.heappush(end,costs[n-i-1])
        sm=0
        lt=candidates-1
        rt=n-candidates
        while k>0:
            x,y=float("infinity"),float("infinity")
            if st:
                x=heapq.heappop(st)
            if y:
                y=heapq.heappop(end)
            if x<=y:
                sm+=x
                lt+=1
                if lt<rt:
                    heapq.heappush(st,costs[lt])
                heapq.heappush(end,y)
            else:
                sm+=y
                rt-=1
                if lt<rt:
                    heapq.heappush(end,costs[rt])
                heapq.heappush(st,x)
            k-=1
        return sm