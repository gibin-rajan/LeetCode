class Solution:
    def searchBST(self, root, val):
        if root is None:
            return None
        if root.val== val:
            return root
        return self.searchBST(root.left, val) if val< root.val else self.searchBST(root.right, val) 