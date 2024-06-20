class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = permutations(nums)
        visited =[]
        for i in l:
            if i not in visited:
                visited.append(i)
        
        return visited