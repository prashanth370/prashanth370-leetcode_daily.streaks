# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path_sum):
            if not node:
                return 0
            path_sum = path_sum * 10 + node.val
            if not node.left and not node.right:
                return path_sum
            return dfs(node.left, path_sum) + dfs(node.right, path_sum)
    
        return dfs(root, 0)

    
    
# Time Complexity:

# The algorithm traverses each node of the binary tree once.
# At each node, constant-time operations are performed.
# Therefore, the time complexity is O(n), where n is the number of nodes in the tree.
# Space Complexity:

# The space complexity is determined by the call stack during the recursive calls.
# In the worst case, if the binary tree is skewed (i.e., all nodes are in one branch), the depth of the call stack can be equal to the height of the tree.
# Since the depth of the tree is limited to 10 (as mentioned in the problem), the maximum space complexity for the call stack is O(h), where h is the height of the tree, which is constant (10 in this case).
# Additionally, no additional data structures are used apart from the call stack during the recursive calls.
# Therefore, the space complexity is O(1).


# Sure, let's walk through the algorithm step by step with the test case [4, 9, 0, 5, 1] to see how it computes the sum of all root-to-leaf numbers.

# The binary tree corresponding to the given list [4, 9, 0, 5, 1] is as follows:

# markdown
# Copy code
#      4
#     / \
#    9   0
#   / \
#  5   1
# Here's how the algorithm iterates through the tree:

# Start with the root: We start with the root node 4.

# DFS on the left child (9): We recursively call dfs(9, 4) to explore the left child of 4. Now, we are at node 9, and the current path sum is 4. We update the path sum to 4 * 10 + 9 = 49 and call dfs(5, 49) to explore the left child of 9.

# DFS on the left child of (5): We are at node 5, and the current path sum is 49. Since 5 is a leaf node, we return 49 as the sum of the root-to-leaf number starting from node 4 and passing through 9 and 5.

# Backtrack to node 9: After calculating the sum for the left child of 9, we backtrack to node 9.

# DFS on the right child of (9): We recursively call dfs(1, 49) to explore the right child of 9. Now, we are at node 1, and the current path sum is 49. Since 1 is a leaf node, we return 49 as the sum of the root-to-leaf number starting from node 4 and passing through 9 and 1.

# Backtrack to node 9: After calculating the sum for the right child of 9, we backtrack to node 9.

# Backtrack to node 4: After calculating the sum for both children of 4, we backtrack to node 4.

# DFS on the right child (0): We recursively call dfs(0, 4) to explore the right child of 4. Now, we are at node 0, and the current path sum is 4. We update the path sum to 4 * 10 + 0 = 40 and call dfs(None, 40) to explore the left and right children of 0, which are both None.

# Encounter a leaf node: Since there are no children of 0, we return the current path sum 40 as the sum of the root-to-leaf number starting from node 4 and passing through 0.

# Backtrack to node 4: After calculating the sum for the right child of 4, we backtrack to node 4.

# Return the final sum: Finally, we return the sum of all root-to-leaf numbers, which is 49 + 49 + 40 = 1026.