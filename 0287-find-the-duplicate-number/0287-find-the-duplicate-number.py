class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # left, right = 0, len(nums) -1
        # while left < right:
        #     if nums[left] == nums[right]:
        #         return nums[left]
        #     else:
        #         return nums[right]
        #     left +=1
        #     right -=1
        # return -1

        d = {}
        for i in nums:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1

        return max(zip(d.values(), d.keys()))[1]



# Time Complexity (TC):

# Iterating through the entire nums array to count the frequency of each element takes O(n) time, where n is the number of elements in the array.
# Finding the maximum frequency value using max() also takes O(n) time because it iterates through the dictionary's values.
# Thus, the overall time complexity is O(n).
# Space Complexity (SC):

# We use a dictionary d to store the frequency of each element. The space required for this dictionary depends on the number of unique elements in nums.
# In the worst case, where all elements are unique, the dictionary will contain n key-value pairs, resulting in O(n) space complexity.
# However, in the given problem statement, there is only one duplicate number, so the dictionary will contain at most n - 1 key-value pairs.
# Thus, the space complexity is O(n).





# To solve this problem without modifying the array nums and using only constant extra space, we can apply a modified form of binary search algorithm.

# Here's the approach:

# We initialize two pointers, low and high, to represent the range of integers (from 1 to n) where we will search for the duplicate.
# We calculate the mid-point mid of the range.
# We count the number of integers in the array nums that are less than or equal to mid.
# If the count is greater than mid, it means the duplicate lies in the lower half of the range; otherwise, it lies in the upper half.
# We update low or high accordingly and repeat the process until we find the duplicate.
# Let's implement this approach:


# def findDuplicate(nums):
#     n = len(nums) - 1
#     low = 1
#     high = n

#     while low < high:
#         mid = (low + high) // 2
#         count = 0

#         for num in nums:
#             if num <= mid:
#                 count += 1

#         if count > mid:
#             high = mid
#         else:
#             low = mid + 1

#     return low

# # Test cases
# nums1 = [1, 3, 4, 2, 2]
# nums2 = [3, 1, 3, 4, 2]
# nums3 = [3, 3, 3, 3, 3]

# print(findDuplicate(nums1))  # Output: 2
# print(findDuplicate(nums2))  # Output: 3
# print(findDuplicate(nums3))  # Output: 3
