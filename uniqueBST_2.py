# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        if n == 1:
            return [[1]]
        else:
            def fact(k:int)->int:
                F=[]
                F.insert(0,1)
                F.insert(1,1)
                for i in range(2,k+1):
                    F.insert(i,(i * F[i-1]))
                temp = F[k]
                del F
                return temp
            
            def piece(combo_trees,key_list,index):
                root = index +1
                while root <= key_list[len(key_list)-1]:
                    
                return combo_trees
            limit = fact(n) # No of trees possible
            key_list = [i for i in range(1,n+1)] # Getting the keylist according to 1 -> No of nodes
            i=0
            tree_list= []
            while(limit>0 and i<=len(key_list)-1):
                root = key_list[i]
                if root == min(key_list):
                    combo_trees = [root,None,None]
                elif root == max(key_list):
                    combo_trees = [root,0,None]
                else:
                    combo_trees = []
                combo_trees = piece(combo_trees,key_list,i)
                tree_list.append(combo_trees)
                limit-=1
            return tree_list