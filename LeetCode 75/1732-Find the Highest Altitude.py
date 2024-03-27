class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        r = [0]
        for i in gain:
            r.append(r[-1]+i)
        return max(r)