class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ls = len(s)
        lt = len(t)
        dp = [[-1 for i in range(lt)] for j in range(ls)]
        return self.count1(s,t,ls-1,lt-1,dp)
    


    def count1(self,s1, s2, ind1, ind2, dp):
    # If we have exhausted s2, we found a valid subsequence
        if ind2 < 0:
            return 1
     # If we have exhausted s1, but not s2, no valid subsequence found
        if ind1 < 0:
            return 0
    
    # If this subproblem has already been solved, return the cached result
        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]
    
    # If the current characters match, we can either choose to leave one character
    # or stay with the current character in s1
        if s1[ind1] == s2[ind2]:
            leaveOne = self.count1(s1, s2, ind1 - 1, ind2 - 1, dp)
            stay = self.count1(s1, s2, ind1 - 1, ind2, dp)
        
        # Store the result in the DP table and return it modulo prime
            dp[ind1][ind2] = (leaveOne + stay)
            return dp[ind1][ind2]
        else:
        # If the characters don't match, we can only skip the character in s1
            dp[ind1][ind2] = self.count1(s1, s2, ind1 - 1, ind2, dp)
            return dp[ind1][ind2]