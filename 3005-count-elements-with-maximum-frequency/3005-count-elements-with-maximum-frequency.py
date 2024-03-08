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