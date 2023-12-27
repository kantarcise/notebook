"""

Alice and Bob have a different total number of candies. You are given 
two integer arrays aliceSizes and bobSizes where aliceSizes[i] is the number 
of candies of the ith box of candy that Alice has and bobSizes[j] is the 
number of candies of the jth box of candy that Bob has.

Since they are friends, they would like to exchange one candy box each so 
that after the exchange, they both have the same total amount of candy. 
The total amount of candy a person has is the sum of the number of 
candies in each box they have.

Return an integer array answer where answer[0] is the number of candies 
in the box that Alice must exchange, and answer[1] is the number of 
candies in the box that Bob must exchange. If there are multiple answers, 
you may return any one of them. It is guaranteed that at least one 
answer exists.

Example 1:

Input: aliceSizes = [1,1], bobSizes = [2,2]
Output: [1,2]

Example 2:

Input: aliceSizes = [1,2], bobSizes = [2,3]
Output: [1,2]

Example 3:

Input: aliceSizes = [2], bobSizes = [1,3]
Output: [2,3]

Constraints:

1 <= aliceSizes.length, bobSizes.length <= 104
1 <= aliceSizes[i], bobSizes[j] <= 105
Alice and Bob have a different total number of candies.
There will be at least one valid answer for the given input.

Takeaway:

Sets are really cool.

"""

class Solution:
    def fairCandySwap_(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # does not work
        # swap boxes so that they have equal fruits
        # [2] [1,3]
        # difference is 2
        # the swap is the half of the difference
        
        sum_al , sum_bob = sum(aliceSizes), sum(bobSizes)
        
        difference = abs(sum_al - sum_bob)
        
        set_alice, set_bob = set(aliceSizes), set(bobSizes)
        
        len_alice, len_bob = len(aliceSizes), len(bobSizes)
        
        if len_alice <= len_bob:
            for i in range(len_alice):
                if (aliceSizes[i] + (difference//2)) in set_bob:
                    return [aliceSizes[i], aliceSizes[i] + (difference//2)] 
        else:
            for i in range(len_bob):
                if (bobSizes[i] + difference//2) in set_alice:
                    return [bobSizes[i] + (difference // 2), bobSizes[i]]
                
                
    def fairCandySwap(self, A, B):
        # just calm down and think man.
        dif = (sum(A) - sum(B)) / 2
        A = set(A)
        for b in set(B):
            if dif + b in A:
                return [dif + b, b]
