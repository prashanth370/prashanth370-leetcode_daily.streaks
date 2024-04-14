# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
        # This condition checks if both p and q are None, 
        # indicating that both trees are empty. If this condition is met, it returns True, indicating that the trees are the same.
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # If both p and q are non-empty and have the same root value, we recursively call the isSameTree function on their left and right subtrees. This recursive call checks 
        # if the left subtrees of p and q are the same and if the right subtrees of p and q are the same. If all these conditions are met, it returns True, indicating that the trees are the same
        return False