class Solution:
    def maximalRectangle(self, matrix: list[list[str]], ans = 0) -> int:

        m, n = len(matrix), len(matrix[0])
        dp = [0]*(n+1)
        
        for i in range(m):
            stk = deque([-1])

            for j in range(n+1):
                if j < n and matrix[i][j] == '1': dp[j]+= 1
                else: dp[j] = 0

                while(dp[stk[0]] > dp[j]):
                    ans = max(ans,dp[stk.popleft()]*(j-stk[0]-1))

                stk.appendleft(j)

        return ans