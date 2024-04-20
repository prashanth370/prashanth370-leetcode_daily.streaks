from collections import deque

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        farmland_groups = []

        def bfs(row, col):
            top_left = [row, col]
            bottom_right = [row, col]
            queue = deque([(row, col)])
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and land[nr][nc] == 1:
                        land[nr][nc] = 0  # Mark as visited
                        bottom_right = [max(bottom_right[0], nr), max(bottom_right[1], nc)]
                        queue.append((nr, nc))
            return top_left + bottom_right

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    farmland_groups.append(bfs(i, j))

        return farmland_groups

    
    
    
#     Time Complexity (TC):

# In the worst case, every cell of the input matrix land needs to be visited to determine the extent of each farmland group.
# For each cell, the BFS function might explore up to four adjacent cells.
# Therefore, the time complexity is O(m * n), where m is the number of rows and n is the number of columns in the input matrix.
# Space Complexity (SC):

# The space complexity is determined by the queue used in the BFS function and the space required for the output.
# In the worst case, the queue might hold all cells of the farmland group, leading to a space complexity of O(m * n).
# Additionally, the space required for the output is O(k), where k is the number of farmland groups.
# Therefore, the overall space complexity is O(m * n + k), where m is the number of rows, n is the number of columns, and k is the number of farmland groups.
# In summary:

    
    
    
    
# Example 1:
# Input: land = [[1,0,0],[0,1,1],[0,1,1]]

# Start with the input matrix land.
# csharp
# Copy code
# [1, 0, 0]
# [0, 1, 1]
# [0, 1, 1]
# Initialize an empty list farmland_groups to store the coordinates of farmland groups.
# Iterate through each cell of the matrix:
# At cell (0, 0) = 1:
# Start BFS from this cell to explore the connected farmland cells.
# The farmland group extends to cell (0, 0) only.
# Add the coordinates of the top left corner (0, 0) and bottom right corner (0, 0) to farmland_groups.
# At cell (0, 1) = 0: Skip as it's not farmland.
# At cell (0, 2) = 0: Skip as it's not farmland.
# At cell (1, 0) = 0: Skip as it's not farmland.
# At cell (1, 1) = 1:
# Start BFS from this cell to explore the connected farmland cells.
# The farmland group extends from cell (1, 1) to cell (2, 2).
# Add the coordinates of the top left corner (1, 1) and bottom right corner (2, 2) to farmland_groups.
# At cell (1, 2) = 1: Skip as it's already part of the farmland group.
# At cell (2, 0) = 0: Skip as it's not farmland.
# At cell (2, 1) = 1: Skip as it's already part of the farmland group.
# At cell (2, 2) = 1: Skip as it's already part of the farmland group.
# Return the farmland_groups list:
# lua
# Copy code
# [[0, 0, 0, 0], [1, 1, 2, 2]]
# This result indicates that there are two farmland groups in the input matrix:

# The first group is a single hectare farmland at coordinates (0, 0).
# The second group extends from coordinates (1, 1) to (2, 2).





