# class Solution:
#     def check(self, nums: List[int]) -> bool:
#         n  = len(nums)

#         if nums == sorted(nums) or nums == sorted(nums, reverse = True):
#             return True
#         for i in range(n-1):
#             if nums[i] > nums[i+1]:
#                 rotated_arr = nums[i+1:] + nums[:i+1]
#                 if rotated_arr == sorted(rotated_arr) or rotated_arr == sorted(rotated_arr, reverse = True):
#                     return True
#         return False


# class Solution:
#     def check(self, nums: List[int]) -> bool:
#         count = 0
#         n = len(nums)
        
#         for i in range(n):
#             if nums[i] > nums[(i + 1) % n]:
#                 count += 1
                
#         return count <= 1


class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums[i:]+nums[:i]==sorted(nums):
                return True
        return False
