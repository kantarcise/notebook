"""
You are given an array people where people[i] is the 
weight of the ith person, and an infinite number of 
boats where each boat can carry a maximum weight of limit. 

Each boat carries at most two people at the same 
time, provided the sum of the weight of those people is 
at most limit.

Return the minimum number of boats to carry every given person.

Example 1:

    Input: people = [1,2], limit = 3

    Output: 1

    Explanation: 1 boat (1, 2)

Example 2:

    Input: people = [3,2,2,1], limit = 3

    Output: 3

    Explanation: 3 boats (1, 2), (2) and (3)

Example 3:

    Input: people = [3,5,3,4], limit = 5

    Output: 4

    Explanation: 4 boats (3), (3), (4), (5)
 
Constraints:

    1 <= people.length <= 5 * 104
    
    1 <= people[i] <= limit <= 3 * 104

Takeaway:

    You can use a deque. 
    
    But before you commit to a solution. Just think:

    "What am I doing that is doable with simpler approaches?"

"""

# weight list
# infinite boats with max load limit
# each boat at most carries 2 people
# at most limit

# sort people
# for everyone, make a new boat and 
# try to append a small person
# when everyone is on board, return boat number

class Solution:
    def numRescueBoats_(self, people: List[int], limit: int) -> int:
        # works but slow
        
        boats = 0 
        people.sort(reverse = True)
        dq = deque(people)
        
        while dq:
            big = dq.popleft()
            new_boat = []
            boats += 1
            new_boat.append(big)
            if (dq and  
                sum(new_boat) + dq[-1] <= limit and
                len(new_boat) <= 1):
                new_boat.append(dq.pop())
                
        return boats
    
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # two pointers
        # big people are in the end
        people.sort()

        i, j = 0, len(people) - 1
        boat = 0

        while i <= j:
            
            if people[j] + people[i] <= limit:
                # move left pointer, we 
                # can board one more
                i+=1
            
            # move right pointer
            # even if this means someone 
            # riding a boat alone
            j -= 1
            
            # added another boat
            boat += 1

        return boat
