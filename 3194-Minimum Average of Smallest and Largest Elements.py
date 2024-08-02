from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        nums.sort()
        min_avg = (nums[0] + nums[-1]) / 2

        for i in range(1, n // 2):
            avg = (nums[i] + nums[n - 1 - i]) / 2
            if avg < min_avg:
                min_avg = avg

        return min_avg