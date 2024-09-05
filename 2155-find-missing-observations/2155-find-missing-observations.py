class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        sum1 = mean * (n+m)
        remaining_sum = sum1 - sum(rolls) 
        avg = remaining_sum //n
        rem = remaining_sum%n
        if avg > 6 or avg <= 0 or (avg == 6 and rem > 0):
            return []
        res = [avg] * n
        for i in range(rem):
            res[i] +=1
        return res
       
        # if remaining_sum < n or remaining_sum > 6*n:
        #     return []
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
      

# class Solution:
#     def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
#         m = len(rolls)
#         sum1 = mean * (n+m) #24
#         for i in range(m):
#             sum1 -= rolls[i]

#         if sum1 < n or sum1 > 6*n:
#             return []
        
#         avg = sum1 // n
#         rem = sum1 % n
#         res = []
#         for i in range(n):
#             if rem > 0:
#                 res.append(avg + 1)
#                 rem -= 1
#             else:
#                 res.append(avg)
#         return res