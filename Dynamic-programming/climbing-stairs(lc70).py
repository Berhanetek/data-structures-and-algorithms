class Solution:
    def climbStairs(self, n: int) -> int:
        val = {0:0, 1:1, 2:2}
        if n in val:
            return val[n]
        first = val[1]
        second = val[2]
        for i in range (3,n+1):
            temp = second
            second = first + second
            first = temp
        return second

# One pass so time complexity is O(n).
# No matter what a constant number of terms are stored so space complexity is O(1).
