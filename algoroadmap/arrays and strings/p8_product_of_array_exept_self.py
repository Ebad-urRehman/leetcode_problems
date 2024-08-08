class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_array = [1]
        right_array = [1]
        ans_array = []

        """
        nums = [1,2,3,4]
        left_array = [1, 1, 2, 6]
        right_arry = [24, 12, 4, 1]

        left array and right array consists of elements that are multiple of left and right side of a single element
        in nums.

        multiplying them in 3rd for loop gives answer
        """
        for i in range(1, len(nums)):
            left_array.append(nums[i-1] * left_array[i-1]) 

        for i in range(len(nums) - 1, 0, -1):
            right_array.insert(0, nums[i] * right_array[i-len(nums)]) 

        for i in range(len(nums)):
            ans_array.append(left_array[i] * right_array[i])

        return ans_array