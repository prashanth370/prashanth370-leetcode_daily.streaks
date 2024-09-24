# class Solution:
#     def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
#         # we will use helper function for finding the longer prefix
#         def longest_prefix(a, b):
#             length = 0
#             for i in range(min(len(a), len(b))):
#                 if a[i] == b[i]:
#                     length +=1
#                 else:
#                     break
            
#             return length

#         max_length = 0
#         for n1 in arr1:
#             for n2 in arr2:
#                 str1 = str(n1)
#                 str2 = str(n2)
#                 max_length = max(max_length, longest_prefix(str1, str2))
#         return max_length


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_number = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, number: str):
        node = self.root
        for digit in number:
            if digit not in node.children:
                node.children[digit] = TrieNode()
            node = node.children[digit]
        node.is_end_of_number = True

    def longest_common_prefix(self, number: str) -> int:
        node = self.root
        length = 0
        for digit in number:
            if digit in node.children:
                length += 1
                node = node.children[digit]
            else:
                break
        return length

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Create a Trie and insert all numbers from arr1
        trie = Trie()
        for num in arr1:
            trie.insert(str(num))

        max_prefix_length = 0

        # For each number in arr2, find the longest common prefix using the Trie
        for num in arr2:
            max_prefix_length = max(max_prefix_length, trie.longest_common_prefix(str(num)))

        return max_prefix_length

