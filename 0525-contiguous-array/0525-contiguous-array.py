class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}
        sum_val = 0
        max_len = 0
        for i, num in enumerate(nums):
            sum_val += 1 if num == 1 else -1
            if sum_val == 0:
                max_len = i + 1
            elif sum_val in mp:
                max_len = max(max_len, i - mp[sum_val])
            else:
                mp[sum_val] = i
        return max_len


























# Intuition
# To find the maximum length of a contiguous subarray with an equal number of 0s and 1s, we can use the concept of prefix sum. Whenever we encounter a 0, we decrement the sum by 1, and whenever we encounter a 1, we increment the sum by 1. If the prefix sum at two indices is the same, it means that the number of 0s and 1s between those two indices is the same. We store these prefix sums along with their indices in a hash map. Then, for each prefix sum encountered, we check if we have seen this sum before. If so, it means that the subarray between the current index and the index where this sum was last encountered has an equal number of 0s and 1s. We calculate the length of this subarray and update the maximum length accordingly.

# Approach
# Initialize a hash map to store prefix sums along with their indices.
# Initialize variables for sum, maximum subarray length, and iterate through the input array.
# For each element in the array, update the sum according to the element (decrement by 1 for 0, increment by 1 for 1).
# If the sum becomes zero at any index, update the maximum length to the current index plus one.
# If the sum is encountered again (which means there is a subarray with equal 0s and 1s between the previous occurrence and the current index), update the maximum length if the current subarray length is greater than the previously stored maximum length.
# Return the maximum subarray length.
# Complexity Analysis
# Time complexity: (O(n)), where (n) is the length of the input array. We traverse the array only once.
# Space complexity: (O(n)), in the worst case, when all elements are distinct and the sum becomes distinct for each index, we would need to store all prefix sums in the hash map.