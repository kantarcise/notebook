"""
You are given an array of integers stones where 
stones[i] is the weight of the ith stone.

We are playing a game with the stones. 

On each turn, we choose the heaviest two stones and smash them together. 

Suppose the heaviest two stones have weights x and y with x <= y. 

The result of this smash is:

    If x == y, both stones are destroyed, and
    
    If x != y, the stone of weight x is destroyed, and the stone 
        of weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. 

If there are no stones left, return 0.

Example 1:

    Input: stones = [2,7,4,1,8,1]
    
    Output: 1
    
    Explanation: 
        
        We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,

        we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,

        we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,

        we combine 1 and 1 to get 0 so the array converts to [1] then 
        that's the value of the last stone.

Example 2:

    Input: stones = [1]
    
    Output: 1
 
Constraints:

    1 <= stones.length <= 30
    
    1 <= stones[i] <= 1000

Takeaway:

    if we use a sorted approach, we have to sort 
    the list every time

    use a max heap, 
    heapify takes o(n)
    every time accessing max heap is o(log n) - possibly 
    running n times

    to make a max heap in Python, just multiply 
    every value with -1

    in the calculations, use the example in your mind.

"""

from heapq import heapify, heappop, heappush

class Solution:

    def lastStoneWeight_(self, stones: "list[int]") -> int:
        # brute force approach
        # did not work
        def smash(seq):
            if len(seq) == 1:
                return seq
            biggest = max(seq)
            seq.remove(biggest)
            second_biggest = max(seq)  # Note: Find the max from the updated seq list.
            
            if biggest == second_biggest:
                seq.remove(second_biggest)
            else:
                seq.append(biggest - second_biggest)
            
            return seq  # Return the modified list
        
        while len(stones) > 2:
            stones = smash(stones)  # Update the stones list

        return stones[0]

    def lastStoneWeight(self, stones: "list[int]") -> int:
        # if we use a sorted approach, we have to sort 
        # the list every time

        # use a max heap, 
        # heapify takes o(n)
        # every time accessing max heap is o(log n) - possibly 
        # running n times

        # to make a max heap in Python, just multiply 
        # every value with -1

        stones = [-elem for elem in stones]
        heapify(stones)

        while len(stones) > 1:
            first = heappop(stones)
            second = heappop(stones)

            if second > first:
                # -5 - - 8 = 3
                # so make it first - second instead of 
                # second - first
                heappush(stones, first - second)

        # if there are not any stones in the sequence
        stones.append(0)
        return abs(stones[0])

if __name__ == "__main__":
    
    sol = Solution()
    print(sol.last_stone_weight(stones = [2,7,4,1,8,1]))
    print(sol.last_stone_weight(stones = [1]))

    print(sol.last_stone_weight(stones = [2,7,4,1,8,1]))
    print(sol.last_stone_weight(stones = [1]))
