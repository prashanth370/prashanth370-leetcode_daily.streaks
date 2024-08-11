

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d={}
        n=len(nums)
        for i in range(1,n+1,1):
            d[i]=0
        for i in nums:
            d[i]+=1
        m=[]
        for k,v in d.items():
            if v==0:
                m.append(k)
        return m