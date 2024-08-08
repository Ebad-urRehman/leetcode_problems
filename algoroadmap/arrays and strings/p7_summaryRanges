class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        slow = 0
        fast = 0
        list = []

        if len(nums) == 0:
            return []
        while fast != len(nums) - 1:
            if slow == fast and nums[fast] != nums[fast+1]-1:
                list.append(f"{nums[fast]}")
                fast += 1
                slow += 1

            elif nums[fast] != nums[fast+1]-1:
                list.append(f"{nums[slow]}->{nums[fast]}")
                fast+=1
                slow = fast

            else:
                fast+=1
        if slow == fast:
            list.append(f"{nums[fast]}")
        else:
            list.append(f"{nums[slow]}->{nums[fast]}")

        return list