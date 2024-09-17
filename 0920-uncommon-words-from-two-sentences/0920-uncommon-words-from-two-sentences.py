# class Solution:
#     def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
#         word1 = s1.split()
#         word2 = s1.split()
#         word_count = {}

#         for w in word1:
#             word_count[w] = word_count.get(w,0) + 1 
#         for w in word2:
#             word_count[w] = word_count.get(w,0) + 1 
#         unique_w = [w for w in word_count if word_count[w] == 1]
#         return unique_w

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split the sentences into words
        words_s1 = s1.split()
        words_s2 = s2.split()
        
        # Combine all words into one list
        all_words = words_s1 + words_s2
        
        # Count the frequency of each word
        word_count = Counter(all_words)
        
        # Find words that occur exactly once
        return [word for word in word_count if word_count[word] == 1]