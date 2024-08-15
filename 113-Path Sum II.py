# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        result = []

        def rec(node, currentSum, path):
            if not node:
                return

            currentSum += node.val
            path.append(node.val)

            if currentSum == targetSum and not node.left and not node.right:
                result.append(list(path))
            else:
                rec(node.left, currentSum, path)
                rec(node.right, currentSum, path)

            path.pop()

        rec(root, 0, [])
        return result