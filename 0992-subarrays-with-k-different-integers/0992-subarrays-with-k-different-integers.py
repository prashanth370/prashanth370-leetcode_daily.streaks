from collections import Counter

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            count = Counter()
            left = right = 0
            distinct = 0
            result = 0

            while right < len(nums):
                if count[nums[right]] == 0:
                    distinct += 1
                count[nums[right]] += 1
                right += 1

                while distinct > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        distinct -= 1
                    left += 1

                result += right - left

            return result

        return atMostK(nums, k) - atMostK(nums, k - 1)
