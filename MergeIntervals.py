class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        """
        Step-1) Create two pointer (p1,p2) , pointing to 0 and 1 index lists
        Step-2) compare of last_of p2 <= first_of_p1 , if true
        Step-3) If step-2 is true -> set first_of_p1 as min_of_both_list's_0th_elem
                and set last_of_p1 as max_of_both_list's_end_elemens
        Step-4) If step-2 is false , just increment both and again do the loop
        """
        p1, p2 = 0, 1
        while p2 <= len(intervals) - 1 and p1 <= p2:
            last_of_p1_interval = intervals[p1][len(intervals[p1]) - 1]
            first_of_p2_interval = intervals[p2][0]
            first_of_p1_interval = intervals[p1][0]
            last_of_p2_interval = intervals[p2][len(intervals[p2]) - 1]
            if first_of_p2_interval <= last_of_p1_interval:
                intervals[p1][0] = min(first_of_p1_interval, first_of_p2_interval)
                intervals[p1][len(intervals[p1]) - 1] = max(
                    last_of_p1_interval, last_of_p2_interval
                )
                temp = p2
                intervals.remove(intervals[temp])
            else:
                p1 += 1
                p2 += 1
                continue
        # print(intervals)
        return intervals


Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
Solution().merge([[1, 4], [0, 2], [3, 5]])
Solution().merge([[1, 4], [4, 5]])
