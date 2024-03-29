class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = []
        for i in intervals:
            if i[1] < newInterval[0]:
                l.append(i)
            elif i[0] > newInterval[1]:
                l.append(newInterval)
                newInterval = i
            else:
                # Merge overlapping intervals
                newInterval[0] = min(newInterval[0], i[0])
                print(newInterval[0])
                newInterval[1] = max(newInterval[1], i[1])
                print(newInterval[1])
        l.append(newInterval)
        return l



