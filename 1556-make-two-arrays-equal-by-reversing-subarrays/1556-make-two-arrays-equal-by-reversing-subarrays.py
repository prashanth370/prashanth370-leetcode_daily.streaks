class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # val = [::-1]
        val = sorted(arr)
        k = sorted(target)

        if k == val:
            return "true"
        "false"
