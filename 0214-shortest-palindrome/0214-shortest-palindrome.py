# class Solution:
#     def shortestPalindrome(self, s: str) -> str:
#         r = s[::-1]
#         for i in range(len(s) + 1):
#             if s.startswith(r[i:]):
#                 return r[:i] + s



class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # l, r = 0, len(s) - 1
        # a a c e c a a a
        if s == s[::-1]:
            return s

        added = ""

        for i in range(len(s) - 1, -1, -1):
            added += s[i]
            val = added + s
            if added + s == val[::-1]:
                return added + s
                break
        return s + s[::-1]