class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnts in count.items():
            freq[cnts].append(num)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

sol = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(sol.topKFrequent(nums, k))
