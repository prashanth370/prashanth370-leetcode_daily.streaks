# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def solve(node, current_depth):
            nonlocal maxdepth, bottom_left

            if not node:
                return 

            if current_depth > maxdepth:
                maxdepth = current_depth
                bottom_left = node.val

            solve(node.left, current_depth+1)
            solve(node.right, current_depth+1)

        maxdepth = -1
        bottom_left = None

        solve(root, 0)
        return bottom_left
