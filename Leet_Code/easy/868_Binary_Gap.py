"""
Given a positive integer n, find and return the longest 
distance between any two adjacent 1's in the binary 
representation of n. If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating 
them (possibly no 0's). The distance between two 1's is 
the absolute difference between their bit positions. 
For example, the two 1's in "1001" have a distance of 3.

Example 1:

Input: n = 22
Output: 2
Explanation: 22 in binary is "10110".
The first adjacent pair of 1's is "10110" with a distance of 2.
The second adjacent pair of 1's is "10110" with a distance of 1.
The answer is the largest of these two distances, which is 2.
Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.

Example 2:

Input: n = 8
Output: 0
Explanation: 8 in binary is "1000".
There are not any adjacent pairs of 1's in the binary representation of 8, so we return 0.

Example 3:

Input: n = 5
Output: 2
Explanation: 5 in binary is "101".

Constraints:

1 <= n <= 109

Takeaway:

bin() mastery.

"""

class Solution:
    def binaryGap(self, n: int) -> int:
        # convert binary
        # find 1 indexes
        # find max distance
        b = bin(n)[2:]
        
        one_index = []
        for i, chr in enumerate(b):
            if chr == "1":
                one_index.append(i)
                
        return self.max_dif(one_index)
    
    def max_dif(self, collection):
        if not collection:
            return 0
        max_dif = 0
        for i in range(len(collection) - 1):
            max_dif = max(max_dif, collection[i+1] - collection[i])
        return max_dif
    
    def binaryGap_(self, n: int) -> int:
        # from a homie
        binary = bin(n)
        binary= binary[2:]
        found = False
        max_count = 0
        
        # one pass
        for i in range(len(binary)):
            # first 1
            if (binary[i]=='1' and found ==False):
                start= i
                found = True
            # another 1 found       
            elif (binary[i]=='1' and found==True):
                count = i- start
                start= i # new start
                if (count > max_count):
                    max_count = count
        return max_count
