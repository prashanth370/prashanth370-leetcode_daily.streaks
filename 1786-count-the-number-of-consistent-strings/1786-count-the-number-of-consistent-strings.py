class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        for word in words:
            if all(char in allowed for char in word):
                c +=1
        return c
        