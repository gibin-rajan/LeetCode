class Solution:
    def checkSubarraySum(self, nums, k):
        first_occur = {0: -1}
        total = 0
        for i, n in enumerate(nums):
            total += n
            total %= k
            if total in first_occur:
                if i - first_occur[total] > 1:
                    return True
            else:
                first_occur[total] = i
        return False