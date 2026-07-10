# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        flag = True
        def inorder(root):
            if root != None:
                inorder(root.left)
                nonlocal prev 
                nonlocal flag
                if prev == None:
                    prev = root.val 
                else:
                    if prev >= root.val:
                        flag = False
                    prev = root.val
                inorder(root.right)
        inorder(root)
        return flag