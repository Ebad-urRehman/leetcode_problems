from array import *
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # method 1
        # size = len(nums)
        # for i in range(size-1):
        #     for j in range(size-1):
        #         if nums[i] + nums[j+1] == target and i != j+1:
        #             return i, j+1
        # print("No such elements found")

        size = len(nums)

        for i in range(size):
            num2 = target - nums[i]
            if num2 in nums and nums.index(num2) != i:
                return i, nums.index(num2)