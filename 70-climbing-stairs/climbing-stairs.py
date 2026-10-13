class Solution(object):
    def climbStairs(self, n):
        first = 1
        second = 1

        for i in range(2, n + 1):
            first, second = second, first + second

        return second
