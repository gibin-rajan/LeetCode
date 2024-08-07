# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dict_level = {}

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.get_level_for_the_node(node=root, level=0)
        answer = []
        values = list(self.dict_level.values())
        for i in range(len(values)):
            if i%2==0:
                answer.append(values[i])
            else:
                answer.append(values[i][::-1])
        return answer

    def get_level_for_the_node(self, node, level):
        if node:
            val = self.dict_level.get(level)
            if val:
                val.append(node.val)
            else:
                self.dict_level[level] = [node.val]
            if node.left:
                self.get_level_for_the_node(node=node.left, level=level+1)
            if node.right:
                self.get_level_for_the_node(node=node.right, level=level+1)
        