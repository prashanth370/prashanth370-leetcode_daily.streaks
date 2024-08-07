from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        forest = []
        
        def helper(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            
            node.left = helper(node.left)
            node.right = helper(node.right)
            
            if node.val in to_delete_set:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None
            
            return node
        
        if helper(root):
            forest.append(root)
        
        return forest
