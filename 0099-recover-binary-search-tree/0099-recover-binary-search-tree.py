# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = self.f = self.s = None
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            if self.prev and self.prev.val>root.val:
                if not self.f:
                    self.f=self.prev
                self.s=root
            self.prev=root
            inorder(root.right)
        inorder(root)
        self.f.val, self.s.val = self.s.val, self.f.val
                

        