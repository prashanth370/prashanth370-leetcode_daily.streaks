class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums[:] = list(set(nums))
        # return len(nums)

        # if not nums:
        #     return 0
        # or

        n = len(nums)
        if n==0:
            return 0

        j = 0
        for i in range(1, n):
            if nums[i] != nums[j]:
                j +=1
                nums[j] = nums[i]
        return j+1
        
        
        
        
        
        
        
        
        
        
        
        
        
        # c=0
        # for i in range(len(nums)):
        #     if i<len(nums)-1 and  nums[i] == nums[i+1]:
        #         continue
        #     nums[c] = nums[i]
        #     c +=1
        # return c 