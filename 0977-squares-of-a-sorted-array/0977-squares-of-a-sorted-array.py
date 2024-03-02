# from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        index = n - 1  # Index to fill result array from the end
        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            
            if left_square > right_square:
                result[index] = left_square
                left += 1
            else:
                result[index] = right_square
                right -= 1
            index -= 1
        
        return result
       

        # square_nums = [num ** 2 for num in nums]
        # square_nums.sort()

        # return square_nums





# square_nums = []
#         for num in nums:
#             square_nums.append(num ** 2)
#         square_nums.sort()
#         return square_nums

