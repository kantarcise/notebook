"""
Koko loves to eat bananas. 

There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. 

Each hour, she chooses some pile of bananas and eats k bananas 
from that pile. If the pile has less than k bananas, she eats all
of them instead and will not eat any 
more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating 
all the bananas before the guards return.

Return the minimum integer k such that she can eat 
all the bananas within h hours.

Example 1:

    Input: piles = [3,6,7,11], h = 8
    Output: 4

Example 2:

    Input: piles = [30,11,23,4,20], h = 5
    Output: 30

Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 
Constraints:

    1 <= piles.length x<= 10^4
    piles.length <= h <= 10^9
    1 <= piles[i] <= 10^9

Takeaways:

    math.ceil for finding the ceiling of a number.

    understanding the question will give you a 
        range for possible k values

    after that, we can apply binary search to that sequence!

    this is cool:
        mid = l + ((r - l) // 2)

"""
import math

class Solution:

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # This causes timeout - does not work.

        # koko can only eat one pile at a time
        # so hours should be bigger than number of piles
        
        # h >= len(piles)

        # brute force approach would be giving k = 1, 2, 3 ..
        
        # if koko can eat max pile at 1 hour,then time would be equal 
        # to number of piles 
        
        # so k is somewhere between 1 and max of the pile.  

        result = None
        for k in range(1, max(piles) + 1):
            total_hours = 0
            
            for elem in piles:
                time_spent_in_a_pile = math.ceil((elem / k))
                total_hours += time_spent_in_a_pile

            if total_hours <= h:
                result = k
                break

        return result

    def minEatingSpeed_(self, piles: list[int], h: int) -> int:
        # we dont have to try every single value of k

        # apply binary search to the k range
        # [3, 6, 7, 11] - h = 8
        # k possibly = 
        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        # in middle, there is 6
        # if we calculate hours for k = 6
        # 1 + 1 + 2 + 2 = 6 
        # Nice. Koko can finish the bananas in time. But is this the 
        #   minimum value k can take? 

        # depending on the given avaliable hours, adjust k.

        # binary search depends on l < r property.

        l, r = 1, max(piles)
        res = r

        while l <= r :
            k = l + ((r-l) // 2)
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                # update the result for current k
                res = min(res, k)
                # rate was too fast, look into the smaller 
                # part of the k's
                r = k - 1
            else:
                # rate was too small, look into the larger 
                # part of the k's
                l = k + 1

        return res

    def minEatingSpeed__(self, piles: list[int], h: int) -> int:
        # here is a tightly packed solution.
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if sum(math.ceil(p / m) for p in piles) > h:
                l = m + 1
            else:
                r = m
        return l


if __name__ == '__main__':
    sol = Solution()

    print(sol.minEatingSpeed(piles = [3,6,7,11], h = 8))
    print(sol.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
    print(sol.minEatingSpeed(piles = [30,11,23,4,20], h = 6))

    print("Faster:")

    print(sol.minEatingSpeed_(piles = [3,6,7,11], h = 8))
    print(sol.minEatingSpeed_(piles = [30,11,23,4,20], h = 5))
    print(sol.minEatingSpeed_(piles = [30,11,23,4,20], h = 6))

    print("even Faster?")

    print(sol.minEatingSpeed__(piles = [3,6,7,11], h = 8))
    print(sol.minEatingSpeed__(piles = [30,11,23,4,20], h = 5))
    print(sol.minEatingSpeed__(piles = [30,11,23,4,20], h = 6))
