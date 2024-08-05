class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        
        for val in arr:
            if val in freq:
                freq[val] +=1
            else:
                freq[val] = 1

        # l = [key for key, value in freq.items() if value == 1]
        
        # # Return the k-th distinct string if it exists, otherwise return an empty string
        # if k <= len(l):
        #     return l[k-1]
        # else:
        #     return ""

        l = []
        for key, value in freq.items():
            if value == 1:
                l.append(key)

        if k <= len(l):
            return l[k-1]
        else:
            return ""



#         l = []
#         for key, values in d.items():
#             if values < 1:
#                 l.append(key)
#         return l