# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):    
        queue = [(p, q)]
        while queue:

            node1, node2 = queue.pop(0)

            if node1 and node2 and node1.val == node2.val:
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))

            elif node1 or node2:
                return False            

        return True