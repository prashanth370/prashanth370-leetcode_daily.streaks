class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        removals = set()
        for i,char in enumerate(s):
            if char =='(':
                stack.append(i)
            elif char ==')':
                if stack:
                    stack.pop()
                else:
                    removals.add(i)
        
        removals.update(stack)

        result = ''
        for i,char in enumerate(s):
            if i not in removals:
                result += char
        return result
