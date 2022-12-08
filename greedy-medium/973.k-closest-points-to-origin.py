#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    # Use min-heap
    def kClosest_2(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        weights = []
        for i in points:
            heapq.heappush(weights, (i[0]**2 + i[1]**2, i))
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(weights)[1])

        return ans
    
    # Clean but slow
    def kClosest_2(self, P, k):
        return sorted(P, key=lambda p: p[0]**2 + p[1]**2)[:k]

    # Dict sort
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        weights = {}

        for i in range(len(points)):
            v2 = points[i]
            weights[i] = v2[0] * v2[0] + v2[1] * v2[1]

        weights = dict(sorted(weights.items(), key=lambda item: item[1]))

        ans = []
        keys = list(weights.keys())
        for i in range(k):
            ans.append(points[keys[i]])

        return ans
        
# @lc code=end

