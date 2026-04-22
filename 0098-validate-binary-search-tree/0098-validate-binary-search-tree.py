# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return True
        # lt=False
        # rt=False
        # ln,rn=float('-inf'),float('inf')
        # if root.left.val:
        #     ln=root.left.val
        # if root.right.val:
        #     rn=root.right.val
        # if root.val>ln:
        #     lt=self.isValidBST(root.left)
        # if root.val<rn:
        #     rt=self.isValidBST(root.right)
        # return lt or rt
        #WRONG ONE NEED TO FIX
        def dfs(root,low,high):
            if not root:
                return True
            if not (low<root.val<high):
                return False
            return dfs(root.left,low,root.val) and dfs(root.right,root.val,high)
        return dfs(root,float('-inf'),float('inf'))