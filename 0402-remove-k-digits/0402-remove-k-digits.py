class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remain = len(num) - k
        for c in num:
            while k and stack and stack[-1] > c:
                stack.pop()
                k -=1
            stack.append(c)

        res =''.join(stack[:remain])
        return res.lstrip('0') or '0'



# Example Walkthrough
# Let's consider a small example to illustrate the solution approach. Suppose the input string num is "1432219" and k is 3. We want to remove 3 digits to make the number as small as possible.

# Here's the step-by-step process:

# Initialize an empty list stk to represent the stack. The number of digits we want to remain in the final number is remain = len(num) - k = 7 - 3 = 4.

# Iterate over each digit in "1432219":

# Start with the first digit '1'. Since the stack is empty, we add '1' to stk.
# Next is '4'. '4' is greater than '1', so we keep it and push '4' to stk.
# Then comes '3'. '3' is smaller than '4' and k > 0, so we pop '4' out of the stack. Now stk = ['1'] and k = 2.
# Now we have '2'. '2' is smaller than '3', so we pop '3'. Now, stk = ['1'] and k = 1.
# Add '2' to the stack. stk = ['1', '2'].
# Another '2' comes, which is the same as the last digit, so we push '2' to stk. stk = ['1', '2', '2'].
# Finally, '1' is smaller than '2', so we pop the last '2' from stk. stk = ['1', '2'], and k = 0 (no more removals allowed).
# Since we've already removed 3 digits, just push '1' and then '9' to the stack. Now, stk = ['1', '2', '1', '9'].
# We've finished processing each digit and our stack stk represents the smallest number we could make. However, we need to make sure we have the right number of digits, which should be remain = 4. Since stk already contains 4 digits, there's no need to slice.

# Join the stack to form a number and strip leading zeros (if any). result = ''.join(stk).lstrip('0'). In this case, '1219'.

# We return '1219', which is the smallest number possible after removing 3 digits from "1432219".

# This example illustrates how the stack helps efficiently manage the digits of the new number, ensuring that smaller digits remain at the higher place values whenever possible.