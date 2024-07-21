import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return true
        
        result = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        return result == result[::-1]
    
        