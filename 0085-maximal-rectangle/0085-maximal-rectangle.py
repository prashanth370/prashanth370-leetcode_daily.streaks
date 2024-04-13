class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        def largestRectangleArea(heights: List[int]) -> int:
            stack = []
            max_area = 0
            heights.append(0)  # Append a zero height to trigger the calculation of the remaining rectangles
            
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
                
            return max_area
        
        max_area = 0
        n = len(matrix)
        m = len(matrix[0])
        heights = [0] * (m + 1)
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_area = max(max_area, largestRectangleArea(heights))
        
        return max_area







# Time Complexity (TC):

# Iterating through each cell in the matrix requires O(rows * cols) operations.
# For each row, the largestRectangleArea function is called, which has a time complexity of O(cols).
# Therefore, the overall time complexity is O(rows * cols^2), where rows is the number of rows and cols is the number of columns in the matrix.
# Space Complexity (SC):

# The space complexity is primarily determined by the heights array, which has a length of cols + 1.
# Additionally, the stack used in the largestRectangleArea function can store up to cols elements.
# Therefore, the space complexity is O(cols).




# matrix = [
#     ["1","0","1","0","0"],
#     ["1","0","1","1","1"],
#     ["1","1","1","1","1"],
#     ["1","0","0","1","0"]
# ]
# We'll go through the iteration for each row of the matrix and the corresponding changes in the heights array.

# First row:

# Iterate through each cell:
# Cell (0, 0): '1' => Update heights[0] to 1.
# Cell (0, 1): '0' => heights[1] remains 0.
# Cell (0, 2): '1' => Update heights[2] to 1.
# Cell (0, 3): '0' => heights[3] remains 0.
# Cell (0, 4): '0' => heights[4] remains 0.
# After the first row, the heights array becomes [1, 0, 1, 0, 0].
# Second row:

# Iterate through each cell:
# Cell (1, 0): '1' => Increment heights[0] to 2.
# Cell (1, 1): '0' => heights[1] remains 0.
# Cell (1, 2): '1' => Increment heights[2] to 2.
# Cell (1, 3): '1' => Increment heights[3] to 1.
# Cell (1, 4): '1' => Increment heights[4] to 1.
# After the second row, the heights array becomes [2, 0, 2, 1, 1].
# Third row:

# Iterate through each cell:
# Cell (2, 0): '1' => Increment heights[0] to 3.
# Cell (2, 1): '1' => Increment heights[1] to 1.
# Cell (2, 2): '1' => Increment heights[2] to 3.
# Cell (2, 3): '1' => Increment heights[3] to 2.
# Cell (2, 4): '1' => Increment heights[4] to 2.
# After the third row, the heights array becomes [3, 1, 3, 2, 2].
# Fourth row:

# Iterate through each cell:
# Cell (3, 0): '1' => Increment heights[0] to 4.
# Cell (3, 1): '0' => heights[1] remains 0.
# Cell (3, 2): '0' => heights[2] remains 0.
# Cell (3, 3): '1' => Increment heights[3] to 3.
# Cell (3, 4): '0' => heights[4] remains 0.
# After the fourth row, the heights array becomes [4, 0, 0, 3, 0].
# Now, we apply the largestRectangleArea function to the heights array, which returns the maximum area of the rectangle. In this case, the maximum area is 6.

# So, the output is 6, which represents the largest rectangle containing only 1's in the given binary matrix.








