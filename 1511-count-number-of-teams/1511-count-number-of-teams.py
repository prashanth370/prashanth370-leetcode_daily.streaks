from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        n = len(rating)
        
        for j in range(n):
            left_less = left_greater = right_less = right_greater = 0
            
            # Count soldiers to the left of j
            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                else:
                    left_greater += 1
            
            # Count soldiers to the right of j
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_less += 1
                else:
                    right_greater += 1
            
            # Calculate the number of valid teams
            count += left_less * right_greater + left_greater * right_less
        
        return count