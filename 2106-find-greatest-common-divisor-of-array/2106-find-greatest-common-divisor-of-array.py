class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # val1 = min(nums)
        # val2 = max(nums)

        # max_divisor = []

        # for i in range(1, val2 + 1):
        #     if i % val1 == 0 and i % val2 == 0:
        #         max_divisor.append(i)

        # if max_divisor:
        #     return max(max_divisor)
        # else:
        #     return None

        def gcd(a,b):
            while b:
                a,b = b, a%b
            return a

        min_value = min(nums)
        max_value = max(nums)

        return gcd(min_value, max_value)
        