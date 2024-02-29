# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue
# class Solution:
#     def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return False
        
#         que = Queue()
#         que.put(root)
#         even_level = True

#         while not que.empty():
#             size = que.qsize()
#             prev_val = None

#             for _ in range(size):
#                 node = que.get()

#                 if even_level:
#                     if node.val % 2 ==0 or (prev_val is not None and prev_val >= node.val):
#                         return False
#                 else:
#                     if node.val % 2 !=0 or (prev_val is not None and prev_val <= node.val):
#                         return False
                
#                 prev_val = node.val
#                 if node.left:
#                     que.put(node.left)
#                 if node.right:
#                     que.put(node.right)

#             even_level = not even_level

#         return True

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        que = deque()
        que.append(root)
        even_level = True
        
        while que:
            n = len(que)
            prev = float('-inf') if even_level else float('inf')
            
            for _ in range(n):
                node = que.popleft()
                
                if even_level:
                    if node.val % 2 == 0 or node.val <= prev:
                        return False
                else:
                    if node.val % 2 == 1 or node.val >= prev:
                        return False
                
                prev = node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                
            even_level = not even_level
        
        return True