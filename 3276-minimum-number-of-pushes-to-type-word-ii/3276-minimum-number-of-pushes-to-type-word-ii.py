class Solution:
    def minimumPushes(self, word: str) -> int:
        # Frequency array for each letter
        freq = [0] * 26
        for c in word:
            freq[ord(c) - ord('a')] += 1
        
        # Sort frequencies in descending order
        freq.sort(reverse=True)
        
        # Find the size of the array without trailing zeroes
        sz = next((i for i, x in enumerate(freq) if x == 0), 26)
        
        # Calculate the minimum pushes
        total_pushes = 0
        for i in range(sz):
            total_pushes += freq[i] * (i // 8 + 1)
        
        return total_pushes
        