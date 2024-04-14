# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, is_left: bool) -> int:
            if not node:
                return 0
            if not node.left and not node.right and is_left:
                return node.val
            return dfs(node.left, True) + dfs(node.right, False)
        return dfs(root, False)
        
            
        
        
        
# Sure, let's go through the process step by step using the example input [3,9,20,null,null,15,7].

# We start with the root node, which has a value of 3.
# We call the dfs function with the root node and is_left=False.
# Inside the dfs function, we check if the node is None, which it's not, so we proceed.
# We check if the node is a leaf node (no left or right child) and if it's a left child (is_left=True). Since it's not a leaf node, we skip this check and proceed to the recursive calls.
# We make a recursive call to dfs(node.left, True) with the left child of the root node (value 9) and is_left=True.
# Inside this recursive call, we encounter a leaf node (9) and it's also a left child, so we return its value, which is 9.
# We return to the previous recursive call where we left off and make a recursive call to dfs(node.right, False) with the right child of the root node (subtree with root 20) and is_left=False.
# Inside this recursive call, we encounter the root node of the subtree (value 20). We repeat steps 3-7 for this subtree.
# We return to the initial call to dfs where we left off and make a recursive call to dfs(node.right, False) with the right child of the root node (value 7) and is_left=False.
# Inside this recursive call, we encounter a leaf node (7), but it's not a left child, so we skip it and return 0.
# We return to the initial call to dfs where we left off, and we add the results of the two recursive calls (9 and 0) and return 9.
# The final result of sumOfLeftLeaves is 9, which is the sum of the left leaves in the binary tree [3,9,20,null,null,15,7].




# Time Complexity (TC):

# In the worst case, the algorithm traverses each node of the binary tree once. Therefore, the time complexity is O(n), where n is the number of nodes in the tree.
# Space Complexity (SC):

# The space complexity is determined by the recursive calls made during the traversal. Since the depth of the recursion depends on the height of the binary tree, in the worst case, when the tree is skewed (like a linked list), the depth of recursion becomes O(n), where n is the number of nodes in the tree.
# Additionally, there's a negligible amount of extra space used for function call stack frames.
# Therefore, the overall space complexity is O(n).





