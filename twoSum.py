class Solution:
    def twoSum(self, nums, target):
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

sol = Solution()
nums = [2, 7, 11, 15]
target = 9
print(sol.twoSum(nums, target))
