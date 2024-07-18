# solution with fast and slow pointer with deletion more time complexity and less space complexity
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums_length = len(nums)
        current_element = nums[0]
        j = 1
        i = 0
        while True:
            if j < len(nums):    
                if nums[i] == nums[j]:
                    del nums[j]
                else:
                    i = j
                    j+=1
            else:
                break

        return len(nums)
    

# solution with fast and slow pointer without deleting less time complexity more memory complexity
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        slow = 0

        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                slow = slow + 1
                nums[slow] = nums[fast]

        return slow + 1
