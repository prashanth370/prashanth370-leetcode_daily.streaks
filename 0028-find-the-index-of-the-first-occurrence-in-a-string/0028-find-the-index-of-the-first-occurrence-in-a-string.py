class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # p1 = 0 
        # p2 = 0
        # while p1 < [len(haystack) - len(needle)+1]:
        #     if haystack[p1] == needle[p2]:
        #         p1 +=1
        #         p2 +=1
        #     else:
        #         p1 +=1
        # if 
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i : i+len(needle)] == needle:
                return i 
        return -1