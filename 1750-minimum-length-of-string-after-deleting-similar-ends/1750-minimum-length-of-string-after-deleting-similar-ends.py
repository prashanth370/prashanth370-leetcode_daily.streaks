class Solution:
    def minimumLength(self, s: str) -> int:
        while len(s) > 1 and s[0] == s[-1]:
            # find the common prefix and suffix
            prefix = ""
            i=0
            while i<len(s) and s[i] == s[0]:
                prefix += s[i]
                i +=1
            
            suffix = ""
            j = len(s)-1
            while j>=0 and s[j] == s[-1]:
                suffix += s[j]
                j -=1

            #  if prefix and suffix both got intersect, we cannot perform any more operation

            if prefix == s and suffix == s:
                return 0

            #  remove common prefix and suffix from the string
            s = s[i:j+1]
        return len(s)
