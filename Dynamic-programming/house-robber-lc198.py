class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums)<3:
            return max(nums)
        max_loot = len(nums) * [0]
        max_loot[0] = nums[0]
        max_loot[1] = max(nums[0], nums[1])
        for i in range (2,len(nums)):
            max_loot[i] = max(max_loot[i-2] + nums[i] , max_loot[i-1])

        return max_loot[-1]
