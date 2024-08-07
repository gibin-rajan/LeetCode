class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        total = sum(nums)
        
        total_diff = 0
        positive_count = 0
        min_abs_diff = float('inf')
        
        for num in nums:
            diff = (num ^ k) - num
            
            if diff > 0:
                total_diff += diff
                positive_count += 1
            min_abs_diff = min(min_abs_diff, abs(diff))
        
        if positive_count % 2 == 1:
            total_diff -= min_abs_diff
        
        return total + total_diff