"""
Given an array of points where points[i] = [xi, yi] represents 
a point on the X-Y plane and an integer k, return the k 
closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean 
distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. 

The answer is guaranteed to be unique (except for the order that it is in).

Example 1:

    Input: points = [[1,3],[-2,2]], k = 1
    
    Output: [[-2,2]]

    Explanation:
        
        The distance between (1, 3) and the origin is sqrt(10).
        The distance between (-2, 2) and the origin is sqrt(8).
        Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.

        We only want the closest k = 1 points from the origin, so 
            the answer is just [[-2,2]].

Example 2:

    Input: points = [[3,3],[5,-1],[-2,4]], k = 2
    
    Output: [[3,3],[-2,4]]

    Explanation: 
    
        The answer [[-2,4],[3,3]] would also be accepted.

Constraints:

    1 <= k <= points.length <= 10^4
    -10^4 <= xi, yi <= 10^4

Takeaway:

    this solution works but it is O(n log n)
    [[1,3],[-2,2]], k = 1
    [[-2, 2]]

    if we can calculate the euclidian distance for every point and
    sort the points list accordingly

    we can return a slice of it.

    heap solution

    we only want k points, we do not have to 
    sort all of the list
    we can use a min heap

    we can calculate for [[1,3],[-2,2]]
    [10, 1, 3], [8, -2, 2]
    put them all in a min heap with heapify - which is o(n)
    and select k items, which would be 
    k log n which would be better than n log n

"""


from heapq import heapify, heappop, _heapify_max

class Solution:

    def kClosest_(self, points: "list[list[int]]", k: int) -> "list[list[int]]":
        # this solution works but it is O(n log n)
        # [[1,3],[-2,2]], k = 1
        # [[-2, 2]]
        
        # if we can calculate the euclidian distance for every point and
        # sort the points list accordingly
        
        # we can return a slice of it.
        points_and_distance = []       
        
        for elem in points:
            # we dont even need to square root because we are just comparing
            dist = (((elem[0] * elem[0]) + (elem[1] * elem[1]) ) **  0.5 )
            points_and_distance.append(elem + [dist])

        print(points_and_distance)

        points_and_distance.sort(key = lambda x : float(x[2]))
        
        # return points_and_distance[k:][0] 

        return [point[:2] for point in points_and_distance[:k]]

    def kClosest(self, points: "list[list[int]]", k: int) -> "list[list[int]]":
        # we only want k points, we do not have to 
        # sort all of the list
        # we can use a min heap

        # we can calculate for [[1,3],[-2,2]]
        # [10, 1, 3], [8, -2, 2]
        # put them all in a min heap with heapify - which is o(n)
        # and select k items, which would be 
        # k log n which would be better than n log n
        
        min_heap = []

        for x, y in points:
            dist_representer = (x * x) + (y * y)
            min_heap.append([dist_representer, x, y])
        
        heapify(min_heap)

        # this is a way to go
        res = []
        while k > 0:
            dist, x, y = heappop(min_heap)
            res.append([x, y])
            k -= 1
        return res

        # this is another way to go
        # return [[x, y] for _, x, y in [heappop(min_heap) for _ in range(k)]]


if __name__ == '__main__':
    sol = Solution()
    print(sol.kClosest(points = [[1,3],[-2,2]], k = 1))
