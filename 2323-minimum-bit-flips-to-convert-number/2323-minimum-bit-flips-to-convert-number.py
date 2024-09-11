class Solution(object):
    def minBitFlips(self, start, goal):
        return bin(start ^ goal).count('1')   


# class Solution:
#     def minBitFlips(self, start: int, goal: int) -> int:
#         ans = 0
#         new = start^goal
#         while new!=0:
#             if new & 1:
#                 ans +=1
#             new >>=1
#         return ans

# class Solution:
#     def minBitFlips(self, start: int, goal: int) -> int:
#         temp = start ^ goal
#         output = 0
#         while temp:
#             if temp & 1:
#                 output += 1
#             temp >>= 1
#         return output
        