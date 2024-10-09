class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Keep track of the unmatched opening and closing parentheses
        open_brackets = 0
        close_brackets = 0
        
        for char in s:
            if char == '(':
                open_brackets += 1
            elif char == ')':
                if open_brackets > 0:
                    # Match a closing bracket with an unmatched opening one
                    open_brackets -= 1
                else:
                    # If no opening bracket is available, we need a new opening one
                    close_brackets += 1

        # Total unmatched parentheses is the sum of unmatched opening and closing brackets
        return open_brackets + close_brackets
