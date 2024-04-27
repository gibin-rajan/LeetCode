import heapq
class SmallestInfiniteSet:
    def __init__(self):
        self.heap=[]
        self.min_num=1
        
    def popSmallest(self):
        if self.heap:
            return heapq.heappop(self.heap)
        self.min_num+=1
        return self.min_num-1
        
    def addBack(self, num):
        if self.min_num>num and num not in self.heap:
            heapq.heappush(self.heap,num)