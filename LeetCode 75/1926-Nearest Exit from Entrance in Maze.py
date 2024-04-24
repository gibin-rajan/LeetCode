from collections import deque
class Solution:
    def nearestExit(self, maze, entrance):

        #### CHECK BORDERS FOR EXITS
        exits = set()
        nrows = len(maze)
        ncols = len(maze[0])
        for i, rows in enumerate(maze):
            if rows[0] == '.':
                exits.add((i, 0))

            if rows[ncols-1] == '.':
                exits.add((i, ncols-1))

        for j in range(ncols):
            if maze[0][j] == '.':
                exits.add((0, j))

            if maze[nrows-1][j] == '.':
                exits.add((nrows-1, j))

        tup_entrance = tuple(entrance)
        exits.discard(tup_entrance)

        if not exits: #sneaky problem
            return -1


        ## BRUTE FORCING
        prev = set() # visit already
        Q = deque()
        Q.append((tup_entrance, 0)) #entrance is enter
        while Q:
            rc, step_cnt = Q.popleft() #track movement number
            if rc in prev: #no visit already
                continue

            r, c = rc
            for rr_cc in [(r-1, c), (r, c-1), (r, c+1), (r+1, c)]: #up down right left start select
                if rr_cc in prev: #no visit already
                    continue

                if rr_cc in exits: #short circuit!
                    return step_cnt + 1

                rr, cc = rr_cc
                if (0 <= rr < nrows) and (0 <= cc < ncols): #not walk off map
                    if maze[rr][cc] == '.':
                        Q.append((rr_cc, step_cnt+1)) #brute force additional movement
            prev.add((r, c))
        return -1