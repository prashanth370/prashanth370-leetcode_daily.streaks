class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq=[0]*101
        max_freq = 0
        for num in nums:
            freq[num] += 1
            max_freq = max(max_freq, freq[num]) 

        ans = 0
        for f in freq:
            if f == max_freq:
                ans += f

        return ans
        





# time compexity = Time Complexity:

# Initialization of freq list: This operation takes constant time because the length of the freq list is fixed to 101, and each element is initialized to 0. So, it's O(1).

# Iterating through the input list nums to update frequencies:

# Since we iterate through each element of nums once, this operation takes O(N) time, where N is the length of the input list nums.
# Within the loop, updating the frequency of each element and updating maxF takes constant time.
# Iterating through the frequency list freq to count elements with maximum frequency:

# This operation takes O(101) time since we iterate through a list of fixed size (101).
# Overall, the time complexity is O(N), where N is the length of the input list nums.

# Space Complexity:

# freq list: We are initializing a list of size 101 to store the frequencies of elements. So, the space complexity for this list is O(101), which simplifies to O(1).

# Other variables like maxF, ans, and loop variables: These variables occupy constant space.

# Therefore, the overall space complexity is O(1), as the extra space used by the algorithm does not depend on the size of the input.

# In summary:

# Time complexity: O(N)
# Space complexity: O(1)



















        # n = []
        # max_freq = 0
        # for num in nums:
        #     freq = nums.count(num)
        #     max_freq = max(freq, max_freq)

        
        # count_max_freq = sum(1 for freq in nums if freq == max_freq)
    
        # return count_max_freq
        
        
        # count_max_freq = 0
        # for freq in nums:
        #     if freq == max_freq:
        #         count_max_freq += 1
        
        # return count_max_freq