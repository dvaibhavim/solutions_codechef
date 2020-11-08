'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 1
    
    def finddepth(self,node,depth):
        if node==None:
            return depth-1
        left_subtree = self.finddepth(node.left,depth+1)
        right_ht = self.finddepth(node.right,depth+1)
        
        if (abs(left_subtree-right_ht)>1):
            self.ans = 0
        return max(left_subtree,right_ht)
    def isBalanced(self, root: TreeNode) -> bool:
        self.finddepth(root,0)
        return self.ans