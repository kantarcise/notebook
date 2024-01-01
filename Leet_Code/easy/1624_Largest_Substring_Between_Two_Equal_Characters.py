"""
Given a string s, return the length of the longest substring 
between two equal characters, excluding the two characters. 
If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.

Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".

Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
 
Constraints:

1 <= s.length <= 300
s contains only lowercase English letters.

Takeaway:

Using a map for characters and their indexes is smart.

"""

from collections import Counter
class Solution:
    def maxLengthBetweenEqualCharacters_(self, s: str) -> int:
        # using the python method
        # base case for -1
        if not list(filter(lambda s: s >1, Counter(s).values())):
            return -1
        
        # Store the indices of each character
        indices = {}
        for i, elem in enumerate(s):
            if elem not in indices:
                indices[elem] = [i]
            else:
                indices[elem].append(i)

        max_length = -1

        # Iterate through the indices and calculate the maximum length
        for indices_list in indices.values():
            if len(indices_list) > 1:
                max_length = max(max_length, indices_list[-1] - indices_list[0] - 1)

        return max_length
    
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # from a homie
        # simply map the characters to their indexes
        char_map = {}
        max_diff = 0

        for index, char in enumerate(s):
            if char in char_map:
                # a possible substring appeared
                diff = index - char_map[char]
                # update the difference
                max_diff = max(max_diff, diff)
            else:
                # set the index of the new found character
                char_map[char] = index

        return max_diff - 1
