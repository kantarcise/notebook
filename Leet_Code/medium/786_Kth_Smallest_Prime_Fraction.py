"""
You are given a sorted integer array arr 
containing 1 and prime numbers, where all 
the integers of arr are unique. 

You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, 
we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. 

Return your answer as an array of integers 
of size 2, where answer[0] == arr[i] and 
answer[1] == arr[j].

Example 1:

    Input: arr = [1,2,3,5], k = 3
    
    Output: [2,5]
    
    Explanation: 
        
        The fractions to be considered in sorted order are:
    
            1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.

            The third fraction is 2/5.

Example 2:

    Input: arr = [1,7], k = 1
    
    Output: [1,7]
    
Constraints:

    2 <= arr.length <= 1000
    
    1 <= arr[i] <= 3 * 104
    
    arr[0] == 1
    
    arr[i] is a prime number for i > 0.
    
    All the numbers of arr are unique and 
    sorted in strictly increasing order.
    
    1 <= k <= arr.length * (arr.length - 1) / 2

Takeaway:

    Brute force - optimized! Heaps.

"""

import heapq

class Solution:
    def kthSmallestPrimeFraction_(self, arr: list[int], 
                                   k: int) -> list[int]:
        # works, but really slow
        
        # sorted array, 1 and primes
        # unique elements
        # brute force would be just to find all fractions 00
        # return the kth one
        fractions = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                fractions.append((arr[i]/arr[j], 
                                  (arr[i], arr[j])))
        # print(fractions)
        fractions.sort(key = lambda x: x[0])
        # print(fractions)
        
        return fractions[k-1][1]
      
    def kthSmallestPrimeFraction(self, arr: list[int], 
                                   k: int) -> list[int]:
        
        # the two pointer approach wont work, 
        # because there are a lot of cases to 
        # consider 
        
        # let's try a heap approach!
        
        pq = []
        
        for j in range(1, len(arr)):
            # push all fractions
            # that are the lowest
            heapq.heappush(pq, (arr[0] / arr[j], 0, j))
        
        # this will be automatically sorted 
        # based on the fractions
        
        # because that's how tuples are sorted
        # (1,2,3) < (2,3,4)
        
        # for k times
        for _ in range(k - 1):
            # pop a value
            _, i, j = heapq.heappop(pq)
            
            if i + 1 < j:
                # between i and j
                # difference is bigger than 1
                # push the element onto heap
                heapq.heappush(pq, 
                               (arr[i + 1] / arr[j], 
                                i + 1, 
                                j))
        
        # min element is at 
        # the root of the heap
        _, i, j = pq[0]
        
        return [arr[i], arr[j]]
    

sol = Solution()
print(sol.kthSmallestPrimeFraction(arr = [1,2,3,5], k = 3))
