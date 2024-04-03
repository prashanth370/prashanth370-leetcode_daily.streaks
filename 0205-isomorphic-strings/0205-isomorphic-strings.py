class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_to_t = {}  # Dictionary to store mappings from s to t
        t_to_s = {}  # Dictionary to store mappings from t to s
        
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            # Check if the current mapping violates any condition
            if (char_s in s_to_t and s_to_t[char_s] != char_t) or \
               (char_t in t_to_s and t_to_s[char_t] != char_s):
                return False
            
            # Update mappings
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s
        
        return True

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # return [*map(s.index, s)] == [*map(t.index, t)]
        