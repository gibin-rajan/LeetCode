# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def build(ino, post):
            if not ino or not post:
                return None
            
            node = TreeNode(post[-1])
            idx_in_ino = ino.index(post[-1])

            node.left = build(ino[:idx_in_ino], post[:idx_in_ino])
            node.right = build(ino[idx_in_ino+1:], post[idx_in_ino:-1])
            return node
        
        return build(inorder, postorder)