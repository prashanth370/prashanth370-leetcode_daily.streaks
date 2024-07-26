class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        L, R = 0, 0
        max_frequency, window_sum = 0, 0

        while R < len(nums):
            window_sum += nums[R]

            # If cost to make all window elements equal to 
            # nums[R] exceeds k, shrink window form left. 
            while (nums[R] * (R - L + 1) > k + window_sum):
                window_sum -= nums[L]
                L += 1
            
            max_frequency = max(max_frequency, R - L + 1)
            R += 1

        return max_frequency 
    
    # O(n log n) time
    # O(n) space, Python's Tim Sort uses Linear Space. 