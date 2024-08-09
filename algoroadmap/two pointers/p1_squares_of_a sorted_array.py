class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # solution using normal approach (more efficient)
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        return sorted(nums)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # less optimal using two pointers
        left = 0
        right = len(nums) - 1

        array = []

        while right >= left:
            if abs(nums[left]) > abs(nums[right]):
                array.append(nums[left]**2)
                left += 1
                print(nums[left])
            else:
                array.append(nums[right]**2)
                right -= 1

        array.reverse()

        return array