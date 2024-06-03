class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # if str[s] == str[t]:
        #     return "0"
        
        t_index = 0
        for char in s:
            if t_index < len(t) and char == t[t_index]:
                t_index +=1

        return len(t) - t_index 
