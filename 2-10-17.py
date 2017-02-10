# Two Sum

given_nums = [2, 5, 5, 11]
target = 10

class Solution(object):

    def two_sum_brute_force(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] is target:
                    return [i, j]

sol = Solution()
print(sol.two_sum_brute_force(given_nums, target))