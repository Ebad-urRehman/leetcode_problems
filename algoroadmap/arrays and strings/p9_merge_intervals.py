class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Approach to solution :
        Sorting intervals based on open intervals first bcz we can do it in nlogn if we do sort otherwise O(n^2)
        now the open interval of first element must be smaller than the upcoming ones.
        so the only condition for not overlapping is if close interval of first must be less than second one opening.
        in such case just append that interval and check for next one.
        
        if 2 intervals are overlapping make it one in else statement

        """
        intervals.sort(key=lambda x: x[0])
        merged_intervals = [intervals[0]]

        for i, interval in enumerate(intervals):
            if merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1] = [merged_intervals[-1][0], max(merged_intervals[-1][1],interval[1])] 

        return merged_intervals