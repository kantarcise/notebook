"""
Alice has some number of cards and she wants to rearrange the 
cards into groups so that each group is of size groupSize, and 
consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written 
on the ith card and an integer groupSize, return true if she 
can rearrange the cards, or false otherwise.


Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

Constraints:

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length

Takeaway:

For counter, we can use a dict, a defaultdict, a Counter

We do not actually have to make the groups, we just have to 
check the conditions.

"""
from collections import Counter
from heapq import heapify, heappop
from collections import defaultdict

class Solution:
    def isNStraightHand__(self, hand: list[int], groupSize: int) -> bool:
        # first try, bad
        # does not work
        
        # each group has group size
        # consists of groupSize consecutive cards.
        
        # we can sort the group
        # take first len / groupsize distinct elements
        # seperate others into other groups
        
        number_of_groups = len(hand) // groupSize
        
        hand.sort()
        current_size = 0
        for card in hand:
            pass
        pass
        
    def isNStraightHand_(self, hand: list[int], groupSize: int) -> bool:
        # neet
        
        # length of hand has to be divisable by groupSize
        if len(hand) % groupSize:
            # cannot make these groups
            return False

        count = Counter(hand)

        # make a heap 
        min_heap = list(count.keys())
        # o(n)
        heapify(min_heap)
        
        while min_heap:
            first = min_heap[0]
            # try to populate the group
            for i in range(first, first + groupSize):
                # starting from the first element of the 
                # group, go until the groupsize
                if i not in count:
                    # if consecutive element does not exist
                    return False
                # decrease count
                count[i] -= 1
                
                if count[i] == 0:
                    if i != min_heap[0]:
                        # the index we are about to pop 
                        # HAVE TO be the min value
                        # otherwise we make a hole in our heap and we lost
                        return False
                    # we have to remove this value from the heap
                    # o(log(n))
                    heappop(min_heap)
        
        # if heap expires, we finished the algorithm
        return True
    
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        """Sorting approach
        Most straight forward."""
        
        # counting with a default dict
        counts = defaultdict(int)
        for n in hand:
            counts[n] += 1

        for key in sorted(counts.keys()):
            while counts[key] > 0:
                # while we have a card in deck                
                for i in range(groupSize):
                    # if we do not have the next one
                    if counts[key + i] == 0:
                        # cannot make the group
                        return False
                    # decrease size for the element
                    counts[key + i] -= 1
        return True