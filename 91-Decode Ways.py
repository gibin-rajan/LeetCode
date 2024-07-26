class Solution:
    def numDecodings(self, s: str) -> int:
        self.ways = 0
        self.memo = {}

        def backtrack(prev_added):
            if prev_added in self.memo:
                return self.memo[prev_added]
            
            if prev_added == len(s)-1:
                self.memo[prev_added] = 1
                return 1
            
            total = 0
            for i in range(1,3):
                if prev_added + i < len(s):
                    string = s[prev_added+1:prev_added+i+1]
                    to_add = int(string)
                    if 1 <= to_add <= 26 and string[0] != "0":
                        total+=backtrack(prev_added + i)
            self.memo[prev_added] = total
            return total
        
        return backtrack(-1)