given_nums = [16, 5, 20, 8, 7, 3, 6]
target = 21

# given_nums = [2, 7, 11, 15]
# target = 9

# given_nums = [3, 3]
# target = 6

class Solution(object):

    def twoSum(self, nums, target):
        tuple_nums = []
        for i in range(0, len(nums)):
            tuple_nums.append((nums[i], i))

        self.nums = sorted(tuple_nums, key=lambda num: num[0])

        smaller = 0
        larger = len(self.nums) - 1
        for i in range(0, len(self.nums)):

            if self.nums[smaller][0] + self.nums[larger][0] is target:
                indexes = []
                if self.nums[smaller][0] is self.nums[larger][0]:
                    for num in tuple_nums:
                        if num[0] is self.nums[smaller][0]:
                            indexes.append(num[1])
                else:
                    for num in tuple_nums:
                        if num[0] is self.nums[smaller][0]:
                            indexes.insert(0, num[1])
                        elif num[0] is self.nums[larger][0]:
                            indexes.insert(1, num[1])
                return indexes

            elif self.nums[smaller][0] + self.nums[larger][0] > target:
                larger -= 1
            elif self.nums[smaller][0] + self.nums[larger][0] < target:
                smaller += 1



sol = Solution()
print(sol.twoSum(given_nums, target))