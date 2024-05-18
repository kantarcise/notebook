"""
You are given an array happiness of 
length n, and a positive integer k.

There are n children standing in a queue, 
where the ith child has happiness 
value happiness[i]. 

You want to select k children from 
these n children in k turns.

In each turn, when you select a child, the 
happiness value of all the children that have 
not been selected till now decreases by 1. 

Note that the happiness value cannot 
become negative and gets decremented 
only if it is positive.

Return the maximum sum of the happiness 
values of the selected children 
you can achieve by selecting k children.

Example 1:

    Input: happiness = [1,2,3], k = 2
    
    Output: 4
    
    Explanation: 
    
        We can pick 2 children in the following way:

            - Pick the child with the happiness 
                value == 3. The happiness value of the 
                remaining children becomes [0,1].

            - Pick the child with the happiness value == 1. 
                The happiness value of the remaining child 
                becomes [0]. Note that the happiness value 
                cannot become less than 0.

        The sum of the happiness values of the 
        selected children is 3 + 1 = 4.

Example 2:

    Input: happiness = [1,1,1,1], k = 2
    
    Output: 1
    
    Explanation: 
    
        We can pick 2 children in the following way:
    
            - Pick any child with the happiness 
                value == 1. The happiness value of the 
                remaining children becomes [0,0,0].

            - Pick the child with the happiness 
                value == 0. The happiness value of the 
                remaining child becomes [0,0].

        The sum of the happiness values of the 
        selected children is 1 + 0 = 1.

Example 3:

    Input: happiness = [2,3,4,5], k = 1
    
    Output: 5
    
    Explanation: 
        
        We can pick 1 child in the following way:
    
            - Pick the child with the happiness 
                value == 5. The happiness value of the 
                remaining children becomes [1,2,3].

        The sum of the happiness values of 
        the selected children is 5.
 
Constraints:

    1 <= n == happiness.length <= 2 * 105
    
    1 <= happiness[i] <= 108
    
    1 <= k <= n


Takeaway:

    Brute force is cool. 
    
    The smart approach is cooler.

"""

from copy import deepcopy

class Solution:
    def maximumHappinessSum_(self, happiness: list[int], 
                             k: int) -> int:
        # ERROR
        # TIME LIMIT EXCEEDED
        # o(n^2) time complexity
        
        def decrease_all(a_list):
            for i in range(len(a_list)):
                if a_list[i] > 0:
                    a_list[i] -= 1
        
        number_of_person = k 
        temp = deepcopy(happiness)
        happiness.sort()
        result = 0
        
        while k > 0:
            result += happiness[-1]
            happiness.pop()
            decrease_all(happiness)
            k -= 1
        
        # undo the effect on input
        happiness = temp
        
        return result
    
    def maximumHappinessSum_(self, happiness: list[int], 
                             k: int) -> int:
        # we would just select 
        # the happiest person
        # and decrease the values from the list
        
        # WE CAN UPDATE A SINGLE INDEX
        # we do not have to update whole list
        
        # o(n log n) time complexity

        happiness.sort(reverse=True)
        
        # time passed
        # and index
        i = 0
        
        res = 0

        while k > 0:
            # update ith value, capped with 0
            happiness[i] = max(happiness[i] - i, 0)
        
            # increase result
            res += happiness[i]
            
            # move time and index
            i += 1
            
            # we selected
            k -= 1

        return res
