"""
Given a string s, sort it in decreasing order based on the 
frequency of the characters. The frequency of a character is 
the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Example 1:

Input: s = "tree"
Output: "eert"

Explanation: 'e' appears twice while 'r' and 't' both appear once.
  So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input: s = "cccaaa"
Output: "aaaccc"

Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
  Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input: s = "Aabb"
Output: "bbAa"

Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
  Note that 'A' and 'a' are treated as two different characters.

Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.

Takeaway:

After you found a solution, you can use a better data structure
to optimize your code!

Which in this case are heaps!

"""
from heapq import heapify, heappop
from collections import Counter

class Solution:
    def frequencySort_(self, s: str) -> str:
        # my first approach
        # works
        c = Counter(s)
        result = []
        for elem, count in sorted(list(c.items()), key = lambda x: x[1], reverse = True):
            for _ in range(count):
                result.append(str(elem))
            
        return "".join(result)
            
    def frequencySort__(self, s: str) -> str:
        # faster solution from a homie, using a heap
        
        # "trbeeff"
        count = Counter(s)
        heap = [(freq, ch) for ch, freq in count.items()]
        print(heap) # [(1, 't'), (1, 'r'), (1, 'b'), (2, 'e'), (2, 'f')]
        heapify(heap)
        print(heap) # [(1, 'b'), (1, 'r'), (1, 't'), (2, 'e'), (2, 'f')]

        sorted_str = ""
        while heap:
            freq, ch = heappop(heap)
            sorted_str = ch * freq + sorted_str
        
        return sorted_str
    
    def frequencySort(self, s: str) -> str:
        # using a heap
        # even faster, with using a list..
        
        # "trbeeff"
        count = Counter(s)
        heap = [(freq, ch) for ch, freq in count.items()]
        # print(heap) # [(1, 't'), (1, 'r'), (1, 'b'), (2, 'e'), (2, 'f')]
        heapify(heap)
        # print(heap) # [(1, 'b'), (1, 'r'), (1, 't'), (2, 'e'), (2, 'f')]

        res = []
        while heap:
            freq, ch = heappop(heap)
            res.append(ch * freq)
        
        return "".join(res[::-1])
