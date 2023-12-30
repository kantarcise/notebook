"""
You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is 
a non-empty string, and move any character from words[i] to any 
position in words[j].

Return true if you can make every string in words equal using 
any number of operations, and false otherwise.

Example 1:

Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.

Example 2:

Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.

Takeaway:

The total number of a character should be distributable for all words.

Counter is great!

To check a container element equaling to something, you can use all()

>>>def check(list):
>>>   return all(i == list[0] for i in list)
>>> print(check(['a', 'b', 'c']))
# False
>>> print(check([1, 1, 1]))
# True

values() or keys() can be used to make iterables:
>>> a = {1:34, 2: 4, 4: 56}
>>> print([ elem for elem in a.values()])
[34, 4, 56]
>>> print([ elem for elem in a.keys()])
[1, 2, 4]

"""
from collections import Counter
class Solution:
    def makeEqual_(self, words: List[str]) -> bool:
        # resulting word which we would equal to is somewhere between the smallest and the biggest
        # the number of words should be totaled to all maps in the words
        
        if len(words) == 1:
            return True  # Single word is always equal to itself

        total = Counter()

        # Count the occurrences of each character in all words
        for elem in words:
            total += Counter(elem)

        # Check if the count of each character is a multiple of the number of words
        return all(count % len(words) == 0 for count in total.values())
    
    def makeEqual__(self, words: List[str]) -> bool:
        # from a homie
        s = "".join(words)
        l = len(words)
        cnt = Counter(s)
        for v in cnt.values():
            if v%l != 0:
                return False
        return True 
    
    def makeEqual___(self, words: List[str]) -> bool:
        # from a homie, not that fast
        joint = ''.join(words)
        set1 = set(joint)
        
        for i in set1 :
            if joint.count(i) % len(words) != 0 : return False 
        return True

    def makeEqual(self, words: List[str]) -> bool:
        # flexing
        return all(c % len(words) == 0 for c in Counter("".join(words)).values())
