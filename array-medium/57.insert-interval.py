#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert_3(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval[0], newInterval[1]
        left, right = [], []

        for i in intervals:
            if i[1] < s:
                left += i,
            elif i[0] > e:
                right += i,
            else:
                s = min(s, i[0])
                e = max(e, i[1])

        return left + [[s, e]] + right

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval[0], newInterval[1]
        left = [i for i in intervals if i[1] < s]
        right = [i for i in intervals if i[0] > e]

        if left + right != intervals:
            s = min(s, intervals[len(left)][0])
            e = max(e, intervals[~len(right)][1])
        return left + [[s, e]] + right
    
    # Brute solution, complex case 
    def insert_1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        count = len(intervals)
        small, big = newInterval[0], newInterval[1]

        if count == 1 and intervals[0][1] < small:
            return intervals + [newInterval]

        if count == 0: return [newInterval]

        start, end = 0, count -1

        while start < end:
            s = intervals[start]
            e = intervals[end]

            if s[1] < small:
                start += 1
                continue
            if e[0] > big:
                end -= 1
                continue

            break
        
        small = min(intervals[start][0], small)
        big = max(intervals[end][1], big)

        print(start, end)
        print(small, big)

        for i in range(end, start, -1):
            del intervals[i]

        if start != end:
            del intervals[start]
        else:
            del intervals[end]

        intervals.insert(start, [small, big])
        return intervals
        
# @lc code=end

