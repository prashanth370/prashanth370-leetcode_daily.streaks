class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # while k>0:
        #     nums = nums[1:] + nums[:1]
        #     k -=1
        # return nums this is left shift

        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]