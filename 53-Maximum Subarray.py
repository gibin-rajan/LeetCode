import sys
class Solution(object):
    def maxSubArray(self, nums):
        maxi = -sys.maxsize - 1
        _sum=0
        for i in range(len(nums)):
            _sum+=nums[i]

            if _sum>maxi:
                maxi=_sum

            if _sum<0:
                _sum=0
        return maxi