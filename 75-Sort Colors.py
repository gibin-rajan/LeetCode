class Solution:
    def sortColors(self, nums):
        l, r = 0, len(nums) - 1
        i = 0
        for i in range(len(nums)):
            while i >= l and i <= r and (nums[i] == 0 or nums[i] == 2):
                if nums[i] == 0:
                    nums[i], nums[l] = nums[l], nums[i]
                    l += 1
                elif nums[i] == 2:
                    nums[i], nums[r] = nums[r], nums[i]
                    r -= 1
        