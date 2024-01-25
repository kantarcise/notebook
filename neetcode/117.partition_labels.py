"""
You are given a string s. We want to partition the string 
into as many parts as possible so that each letter appears 
in at most one part.

Note that the partition is done so that after concatenating 
all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.


Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.

A partition like "ababcbacadefegde", "hijhklij" is incorrect, because 
it splits s into less parts.

Example 2:

Input: s = "eccbbbbdec"
Output: [10]

Constraints:

    1 <= s.length <= 500
    s consists of lowercase English letters.

Takeaway:

Partitions are CONTINUOUS.

If an element is in a partition, it has to be in it to win it.

A dictionary for element - lastindex is cool.

"""

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        
        # we will be returning length of the parts
        # partitions are contiguous!
        last_occurance = {} # element : last_occurance

        for i, c in enumerate(s):
            last_occurance[c] = i
            
        result = []
        size, end = 0, 0
        for i, c in enumerate(s):
            # increment size at each step
            size += 1
            # potentially increment end too
            # if last_occurance[c] > end:
            #     end = last_occurance[c]
                
            # we can use max
            end = max(end, last_occurance[c])
            
            # if index reached to end, we can stop 
            # and make a partition
            if i == end:
                result.append(size)
                # we do not have to reset end, we are 
                # already there!
                # size, end = 0, 0
                size = 0
        return result