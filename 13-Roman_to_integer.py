class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        currSum = 0
        num_map = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
        }

        while i < len(s):
            if s[i:i+2] in num_map:
                currSum += num_map[s[i:i+2]]
                i += 2
            else:
                currSum += num_map[s[i]]
                i = i + 1
        return currSum  