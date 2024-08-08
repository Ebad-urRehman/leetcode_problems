class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_counter = 0
        for stone in stones:
            if stone in jewels:
                jewels_counter+=1

        return jewels_counter
    
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        jewels_counter = 0
        for stone in stones:
            if stone in jewels_set:
                jewels_counter+=1

        return jewels_counter
    


"""
Set uses hash map in 2nd case
resulting in timecomplexity O(1) according to gpt

but according to leetcode test both time and space complexity is wildly improved in 1st case without using set 🤷‍♂️
"""

nums = [1,2,3,4]
for i in range(len(nums), 0, -1):
    poped_element = nums.pop()
    print(nums, poped_element)
    if poped_element in nums:
        print(True)

print(False)