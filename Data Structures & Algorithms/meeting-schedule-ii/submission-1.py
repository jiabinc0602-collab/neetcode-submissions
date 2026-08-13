"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startPtr, endPtr = 0, 0
        start = sorted([interval.start for interval in intervals])
        # [0, 5, 15]
        end = sorted([interval.end for interval in intervals])
        # [40, 10, 20]
        minRooms, concurrent = 0, 0
        while startPtr < len(start):
            if start[startPtr] < end[endPtr]:
                concurrent += 1
                startPtr += 1
            else:
                concurrent -= 1
                endPtr += 1
            minRooms = max(concurrent, minRooms)
        
        return minRooms