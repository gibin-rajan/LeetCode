class Solution:
    def dfs(self, nums, idx, k, mp):
        if idx == len(nums):
            return 1

        taken = 0
        if mp[nums[idx] - k] == 0 and mp[nums[idx] + k] == 0:
            mp[nums[idx]] += 1
            taken = self.dfs(nums, idx + 1, k, mp)
            mp[nums[idx]] -= 1
        
        notTaken = self.dfs(nums, idx + 1, k, mp)
        
        return taken + notTaken

    def beautifulSubsets(self, nums, k):
        mp = defaultdict(int)
        ans = self.dfs(nums, 0, k, mp)
        return ans - 1