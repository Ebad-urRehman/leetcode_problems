class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Approach to solution : 
        traversing in reverse
        poping element and checking if same element exist in list then returing true
        if all element poped and nothing remains this mean no elements having a duplicate returning false
        
        Not working because time limit exeeceded in some cases, and very slow by bruteforce method
        so we have to use hash maps like below.
        """
        for i in range(len(nums), 0, -1):
            poped_element = nums.pop()
            if poped_element in nums:
                return True

        return False

# this will work efficiently
# adding into the hash
# if another one encounter that is already in the hash this means list contains duplicates so return true
# otherwise after whole search return false(as their is no duplicates)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_nums = set()

        for num in nums:
            if num not in hash_nums:
                hash_nums.add(num)
            else:
                return True

        return False
    