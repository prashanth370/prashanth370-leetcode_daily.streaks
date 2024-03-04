
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # Find the length of tokens
        n = len(tokens)
        
        # Sort the tokens in ascending order
        tokens.sort()
        
        # Initialize variables
        max_score = 0
        score = 0
        i, j = 0, n - 1
        
        # Iterate through the tokens
        while i <= j:
            # If current power is greater than or equal to the value of token i
            if power >= tokens[i]:
                # Play token i face-up
                power -= tokens[i]
                score += 1
                i += 1
                # Update maximum score if needed
                max_score = max(max_score, score)
            # If current score is at least 1
            elif score >= 1:
                # Play token j face-down
                power += tokens[j]
                score -= 1
                j -= 1
                # Update maximum score if needed
                max_score = max(max_score, score)
            else:
                # If neither condition is satisfied, break the loop
                break
        
        # Return the maximum score achieved
        return max_score

