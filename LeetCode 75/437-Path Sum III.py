class Solution:
    def pathSum(self, root, targetSum):
        self.count = 0
        self.prefix_sum = {0: 1}
        self.dfs(root, targetSum, 0)
        return self.count
        
    def dfs(self, node, targetSum, curr_sum):
        if not node:
            return
        
        curr_sum += node.val
        self.count += self.prefix_sum.get(curr_sum - targetSum, 0)
        self.prefix_sum[curr_sum] = self.prefix_sum.get(curr_sum, 0) + 1
        
        self.dfs(node.left, targetSum, curr_sum)
        self.dfs(node.right, targetSum, curr_sum)
        
        self.prefix_sum[curr_sum] -= 1