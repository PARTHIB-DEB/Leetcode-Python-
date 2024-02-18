# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        answer=[]
        def sum_greater_rootval(value:int,answer:list[int])->int:
            result=0
            for i in range(value,len(answer)):
                result=result+answer[value]
            return result
        stack=[]
        while(1):
            if root:
                stack.append(root)
                root=root.left
            else:
                if not stack:
                    return
                else:
                    root=stack.pop()
                    answer.append(root.val)
                    root=root.right
        while(1):
            if root:
                root.val=sum_greater_rootval(root.val,answer)
                root=root.left
            else:
                if not stack:
                    return
                else:
                    root.val=sum_greater_rootval(root.val,answer)
                    root=root.right
        return root

        

obj=Solution()
root=TreeNode(val=4)
root.left=TreeNode(val=1)
root.right=TreeNode(val=6)
root_left,root_right=root.left,root.right
root_left.left=TreeNode(val=0)
root_left.right=TreeNode(val=2)
root_left_right=root_left.right
root_left_right.right=TreeNode(val=3)
root_right.left=TreeNode(val=5)
root_right.right=TreeNode(val=7)
root_right_right=root_right.right
root_right_right.right=TreeNode(val=8)
obj.bstToGst(root=root)
