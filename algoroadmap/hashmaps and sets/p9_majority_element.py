class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency_dict = {}

        for num in nums:
            if num not in frequency_dict:
                frequency_dict[num] = 1
            else:
                frequency_dict[num] += 1
        
        majority_size = len(nums) // 2

        max_key = max((num for num in frequency_dict if frequency_dict[num] >= majority_size), key=frequency_dict.get, default=None)

        return max_key

