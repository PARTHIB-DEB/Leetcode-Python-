# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(rootnode,left,right):
            if rootnode is None:
                return True
            elif not(rootnode.val > left and rootnode.val < right):
                return False
            else:
                return (validate(rootnode.left,left,rootnode.val) and validate(rootnode.right,rootnode.val,right))

        return validate(root,float("-inf"),float("inf"))
                    
        