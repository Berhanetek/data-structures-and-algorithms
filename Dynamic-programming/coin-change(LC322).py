class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        if amount in coins: return 1
        min_table = {}
        for c in coins:
            min_table[c] = 1
        for i in range(amount+1):
            # if i < min(coins):
            #     min_table[i] = -1
            #     continue
            # the above block of code is not needed. checking len(opts) is enough.
            if i in coins:
                continue
            opts = []
            for c in coins:
                if c < i:
                    if min_table[i-c] != -1:
                        opts.append(1 + min_table[i-c])
            if len(opts) == 0:
                min_table[i] = -1    
            else: min_table[i] = min(opts)
        return min_table[amount]
