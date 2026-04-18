# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,curr,target):
            if not root:
                return False
            if not root.right and not root.left:
                if curr+root.val==target:
                    return True
                return False
            left=right=False
            if root.right:
                right=dfs(root.right,curr+root.val,target)
            if root.left:
                left=dfs(root.left,curr+root.val,target)
            return right or left
        return dfs(root,0,targetSum)