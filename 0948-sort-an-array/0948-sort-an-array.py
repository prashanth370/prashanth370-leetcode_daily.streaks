# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         for i in range(n):
#             for j in range(0, n-i-1):
#                 if nums[j] > nums[j+1]:
#                     nums[j], nums[j+1] = nums[j+1], nums[j]


#         return nums
class Solution:
    def sortArray(self, nums):
        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                left_half = arr[:mid]
                right_half = arr[mid:]

                merge_sort(left_half)
                merge_sort(right_half)

                i = j = k = 0
                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        arr[k] = left_half[i]
                        i += 1
                    else:
                        arr[k] = right_half[j]
                        j += 1
                    k += 1

                while i < len(left_half):
                    arr[k] = left_half[i]
                    i += 1
                    k += 1

                while j < len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1

        merge_sort(nums)
        return nums