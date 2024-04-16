# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        self._addRow(root, val, depth, 1)
        return root
    
    def _addRow(self, node: TreeNode, val: int, depth: int, current_depth: int):
        if not node:
            return
        
        if current_depth == depth - 1:
            # Insert new nodes at the desired depth
            temp_left = node.left
            temp_right = node.right
            node.left = TreeNode(val)
            node.right = TreeNode(val)
            node.left.left = temp_left
            node.right.right = temp_right
        else:
            # Recur for left and right subtrees
            self._addRow(node.left, val, depth, current_depth + 1)
            self._addRow(node.right, val, depth, current_depth + 1)