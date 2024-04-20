from collections import deque, defaultdict
class Solution:
    def canVisitAllRooms(self, rooms):
        q = deque(rooms[0])   #deque -> doubly ended queue
        visited = defaultdict(int)
        visited[0]=1
        count = 1  #to keep a count of unique number of rooms visited
        while q:
            room = q.popleft()  #poping first element
            if room not in visited:
                visited[room] = 1
                count+=1
                q+=rooms[room]
        if count==len(rooms):
            return True
        return False