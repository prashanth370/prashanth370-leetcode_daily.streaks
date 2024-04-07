class Solution:
    def checkValidString(self, s: str) -> bool:
        left_s = []
        star_s = []

        for i, char in enumerate(s):
            if char == '(':
                left_s.append(i)
            elif char == '*':
                star_s.append(i)
            elif char == ')':
                if left_s:
                    left_s.pop()
                elif star_s:
                    star_s.pop()
                else:
                    return False
        
        while left_s and star_s:
            if left_s[-1] < star_s[-1]:
                left_s.pop()
                star_s.pop()
            else:
                break
        return len(left_s) ==0













# Let's walk through the iteration process for the input string s = "(*)".

# Initialize the left stack and star stack as empty lists.

# left_stack = []
# star_stack = []
# Begin iterating through the characters of the string s.

# Step 1: i = 0, char = '('

# Since char is '(', push its index (0) to the left_stack.
# left_stack = [0]
# Step 2: i = 1, char = '*'

# Since char is '*', push its index (1) to the star_stack.
# star_stack = [1]
# Step 3: i = 2, char = ')'

# Since char is ')', try to pop from left_stack first. It is successful as left_stack is not empty.
# left_stack = []
# Step 4: End of iteration.

# After processing all characters, there are no unmatched '(' left in left_stack, and no unmatched '*' in star_stack. Therefore, the string is valid.

# Return True.

# So, for the input string (*), the function would return True as it's a valid parenthesis string.






# Time Complexity (TC):

# The time complexity of the solution is O(n), where n is the length of the input string s.
# This is because the algorithm iterates through each character of the string once.
# Operations within the loop, such as pushing and popping from stacks, and accessing the last element of the stack (left_stack[-1] and star_stack[-1]), are all constant time operations.
# The while loop that pairs up the remaining unmatched '(' with '*' also contributes to O(n) time complexity, as it iterates through the left_stack and star_stack at most once.
# Space Complexity (SC):

# The space complexity of the solution is also O(n), where n is the length of the input string s.
# This is because the algorithm uses two stacks (left_stack and star_stack) to keep track of indices of left parentheses and stars.
# In the worst case, both stacks could hold all characters of the input string.
# However, in most cases, the space used will be less than or equal to the length of the input string.