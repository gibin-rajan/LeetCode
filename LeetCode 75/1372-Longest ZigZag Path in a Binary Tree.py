# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root):
        
        def zz(node, current_direction, previous_direction, current):
            if not node:
                return current
            elif current_direction == "start" and previous_direction == "start":
                current = 0
            elif current_direction != previous_direction:
                current += 1
            else:
                current = 1
            return max(zz(node.left, "left", current_direction, current), \
                zz(node.right, "right", current_direction, current))

        return zz(root, "start", "start", 0)
        