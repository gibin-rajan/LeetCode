class Solution:
    def isMatch(self, s, p):
        memo = [[None] * (len(p) + 1) for _ in range(len(s) + 1)]
        return self.f(s, 0, p, 0, memo)
    
    def f(self, s, i, p, j, memo):
        if i == len(s) and j == len(p):
            return True
        if j == len(p): 
            return False
        
        if memo[i][j] is None:
            flag = False

            if i < len(s) and (s[i] == p[j] or p[j] == '?'): 
                flag = self.f(s, i + 1, p, j + 1, memo)

            elif p[j] == '*':
                for t in range(i, len(s) + 1):
                    if self.f(s, t, p, j + 1, memo):
                        flag = True
                        break
            memo[i][j] = flag

        return memo[i][j]