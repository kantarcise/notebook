"""
You are given an integer array heights representing 
the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to 
the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal 
to the next building's height, you do not 
need a ladder or bricks.

If the current building's height is less than the 
next building's height, you can either use one 
ladder or (h[i+1] - h[i]) bricks.

Return the furthest building index (0-indexed) you can 
reach if you use the given ladders and bricks optimally.

Example 1:

Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4

Explanation: Starting at building 0, you can follow these steps:
  - Go to building 1 without using ladders nor 
        bricks since 4 >= 2.
  - Go to building 2 using 5 bricks. You must use either 
        bricks or ladders because 2 < 7.
  - Go to building 3 without using ladders 
        nor bricks since 7 >= 6.
  - Go to building 4 using your only ladder. You must 
        use either bricks or ladders because 6 < 9.
  
  It is impossible to go beyond building 4 because you 
      do not have any more bricks or ladders.

Example 2:

Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7

Example 3:

Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3
 
Constraints:

  1 <= heights.length <= 105
  1 <= heights[i] <= 106
  0 <= bricks <= 109
  0 <= ladders <= heights.length

Takeaway:

Brute force deos not work, not intelligent

We need a data structure to add the intelligence.

Heaps!

"""

from heapq import heappush, heappop

class Solution:
    def furthestBuilding_(self, heights: List[int], bricks: int, ladders: int) -> int:
        # my approach
        # DOes not work, 
        
        # need a way to add intelligence
        
        # i want to use ladders at last if possible
        # or huge differences
        
        # heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
        # [1,5,1,2,3,4,10000] 4  1
        
        # brute force
        
        for i in range(len(heights) - 1):
            
            diff = heights[i + 1] - heights[i]
            
            if diff <= 0:
                # next building is shorter
                continue
            
            # have to use bricks or ladder
            # try bricks first
            if bricks - diff >= 0:
                bricks -= diff
            elif ladders:
                ladders -= 1
            else:
                return i

        return len(heights) - 1
    
    
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # neet
        
        # - using negative values for max heap
        heap  = [] # max heap of bricks 
        
        for i in range(len(heights) - 1):
            # the difference
            diff = heights[i + 1] - heights[i]
            # if you are at a taller building
            if diff <= 0:
                continue
                
            # use bricks always
            bricks -= diff
            heappush(heap, -diff)
            # if not enough bricks
            if bricks < 0:
                # if no more ladders aswell
                if ladders == 0:
                    # end of the run
                    return i
                # use ladder
                ladders -= 1
                # put back the bricks
                bricks += -heappop(heap)
        
        # if traverse complete, just return last index
        return len(heights) - 1
