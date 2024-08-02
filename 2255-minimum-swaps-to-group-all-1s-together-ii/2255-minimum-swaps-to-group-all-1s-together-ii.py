# class Solution:
#     def minSwaps(self, nums: List[int]) -> int:
        
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        count_ones = nums.count(1)
        
        # Create a window of size count_ones and calculate the number of 0's in it
        max_ones_in_window = 0
        current_ones_in_window = 0
        for i in range(count_ones):
            if nums[i] == 1:
                current_ones_in_window += 1
        max_ones_in_window = current_ones_in_window
        
        # Sliding window over the circular array
        for i in range(1, n):
            if nums[i - 1] == 1:
                current_ones_in_window -= 1
            if nums[(i + count_ones - 1) % n] == 1:
                current_ones_in_window += 1
            max_ones_in_window = max(max_ones_in_window, current_ones_in_window)
        
        # The number of swaps needed is the number of 0's in the window with the most 1's
        min_swaps = count_ones - max_ones_in_window
        return min_swaps