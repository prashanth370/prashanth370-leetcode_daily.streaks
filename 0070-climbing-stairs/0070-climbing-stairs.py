class Solution:
    def climbStairs(self, n: int) -> int:
        w = [0] * (n+1)
        w[0] = 1
        w[1]=1
        for i in range(2, n+1):
            w[i] = w[i-1] + w[i-2]
        return w[n]


        # if n == 1 or n == 0:
        #     return 1
        # else:
        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)



