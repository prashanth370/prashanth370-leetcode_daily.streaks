class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mini = arrays[0][0]
        maxi = arrays[0][-1]
        d = 0
        for i in range(1, len(arrays)):
            d = max(d, abs(arrays[i][-1] - mini), abs(maxi - arrays[i][0]))

            mini = min(mini, arrays[i][0])
            maxi = max(maxi, arrays[i][-1])

        return d

