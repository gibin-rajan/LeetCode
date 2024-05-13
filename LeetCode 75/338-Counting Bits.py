class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l=[]
        for i in range(n+1):
            a=str(bin(i)[2:])
            l.append(a.count('1'))
        return l