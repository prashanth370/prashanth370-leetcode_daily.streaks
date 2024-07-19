class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res = []
        maxCol = []
        m = len(matrix)
        n = len(matrix[0])

        for c in range(n):
            maxCol.append(max(matrix[r][c] for r in range(m)))
        
        for r in range(m):
            minVal = min(matrix[r])
            minIndex = matrix[r].index(minVal)
            if minVal == maxCol[minIndex]:
                res.append(minVal)

        return res