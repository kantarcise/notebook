"""
A triplet is an array of three integers. 

You are given a 2D integer array triplets, 
where triplets[i] = [ai, bi, ci] describes the ith triplet. 

You are also given an integer array target = [x, y, z] that 
describes the triplet you want to obtain.

To obtain target, you may apply the following operation on 
triplets any number of times (possibly zero):

    Choose two indices (0-indexed) i and j (i != j) and update 
    triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].

        For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], 
        triplets[j] will be updated 
        to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].

Return true if it is possible to obtain the target triplet [x, y, z] 
as an element of triplets, or false otherwise.

Example 1:

    Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]

    Output: true

    Explanation: Perform the following operations:

        - Choose the first and last triplets [[2,5,3],[1,8,4],[1,7,5]]. 
        
        Update the last triplet to be 
            [max(2,1), max(5,7), max(3,5)] = [2,7,5]. 
        
        triplets = [[2,5,3],[1,8,4],[2,7,5]]

    The target triplet [2,7,5] is now an element of triplets.

Example 2:

    Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]

    Output: false

    Explanation: 
    
        It is impossible to have [3,2,5] as an element 
        because there is no 2 in any of the triplets.

Example 3:

    Input: 
    
        triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]

    Output: true
    
    Explanation: 
        Perform the following operations:
        
        - Choose the first and third triplets 
        [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]. Update the third triplet to 
        be [max(2,1), max(5,2), max(3,5)] = [2,5,5].
        triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].

        - Choose the third and fourth triplets 
        [[2,5,3],[2,3,4],[2,5,5],[5,2,3]]. Update the fourth 
        triplet to be [max(2,5), max(5,2), max(5,3)] = [5,5,5]. 
        triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]].

        The target triplet [5,5,5] is now an element of triplets.

Constraints:

    1 <= triplets.length <= 10^5
    
    triplets[i].length == target.length == 3
    
    1 <= ai, bi, ci, x, y, z <= 1000

Takeaway:

    Understanding the condition where we can get 
    the target is key

    Some elements are forbidden

    Some are the good ones.
"""
class Solution:
    
    def mergeTriplets_(self, triplets: list[list[int]], target: list[int]) -> bool:
        # from a homie 
        
        # Nice and clean problem where one idea can solve all. 
        # The idea is to take as much tuples as possible, but keep in mind 
        # that some of them are forbidden. By forbidden I mean, that if 
        # we take this tuple, then maximum in one of the 3 places will be 
        # greater that what we need to get. 
        
        # So, algorithm looks like this:

        # Iterate over all triplets once and create forbidden set.
        # Iterate over all triplets once again and update maximums.
        # Check that what we have in the end is equal to what we want.
        forbidden = set()
        for i, [x, y, z] in enumerate(triplets):
            if x > target[0] or y > target[1] or z > target[2]:
                forbidden.add(i)
        
        a, b, c = 0, 0, 0
        for i, (x, y, z) in enumerate(triplets):
            if i not in forbidden:
                a, b, c = max(a, x), max(b, y), max(c, z)
                
        return [a, b, c] == target
    
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        # this works
        good = set()
        
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                # goes over, we cannot use this
                continue
                
            # otherwise, might contain the values we are looking for
            for i, v in enumerate(t):
                # if the element v matches the target at the ith index
                if v == target[i]:
                    # we got the position i from current triplet
                    good.add(i)
        # we want the all 3 to exist
        return len(good) == 3
