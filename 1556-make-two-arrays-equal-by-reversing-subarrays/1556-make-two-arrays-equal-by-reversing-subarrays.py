class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # val = [::-1]
        # return sorted(target) == sorted(arr)


        # val = sorted(arr)
        # k = sorted(target)

        if sorted(target) == sorted(arr):
            return "true"
        "false"
