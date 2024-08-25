# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def traverse(node):
            if node:
                # Traverse the left subtree
                traverse(node.left)
                
                # Traverse the right subtree
                traverse(node.right)
                
                # Visit the root node (append its value to the result list)
                result.append(node.val)
        
        traverse(root)
        return result
