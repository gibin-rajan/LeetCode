# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s=[]
        def bfs(node,level):
            if not node :
                return 
            if len(s) <= level :
                s.append(node.val)
            bfs(node.right,level+1)
            bfs(node.left,level+1)
        bfs(root,0)
        return s
        