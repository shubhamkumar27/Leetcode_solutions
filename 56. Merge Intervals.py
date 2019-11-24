'''
Given a collection of intervals, merge all overlapping intervals.

Example 1: 
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition 
to get new method signature.
'''

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        res = []
        if len(intervals)<=1:
            return intervals
        for interval in intervals:
            if len(res)==0:
                res.append(interval)
            else:
                if interval[0]<=res[-1][-1]:
                    res[-1][-1]=max(interval[-1],res[-1][-1])
                else:
                    res.append(interval)
        return res