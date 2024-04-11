# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def findleaf(root):
            left = []
            right = []
            if root.left == None and root.right == None:
                return [root.val]
            else:
                if root.left != None:
                    left = findleaf(root.left)
                if root.right != None:
                    right = findleaf(root.right)
                return (left + right)

        leaf1 = findleaf(root1)
        leaf2 = findleaf(root2)

        return leaf1 == leaf2