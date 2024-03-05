"""
Given a string s consisting only of 
characters 'a', 'b', and 'c'. You are asked to apply 
the following algorithm on the string any number 
of times:

Pick a non-empty prefix from the string s where 
all the characters in the prefix are equal.

Pick a non-empty suffix from the string s where 
all the characters in this suffix are equal.

The prefix and the suffix should not intersect 
at any index.

The characters from the prefix and suffix 
must be the same.

Delete both the prefix and the suffix.

Return the minimum length of s after performing the 
above operation any number of times (possibly zero times).

Example 1:

Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the 
string stays as is.

Example 2:

Input: s = "cabaabac"
Output: 0

Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".

Example 3:

Input: s = "aabccabba"
Output: 3

Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
 
Constraints:

  1 <= s.length <= 105
  s only consists of characters 'a', 'b', and 'c'.

Takeaway:

  Great question to work on two pointers, deque

"""

from collections import deque

class Solution:
    def minimumLength_(self, s: str) -> int:
        # my first solution, Does not work
        # gotta work on conditions 
        # only a - b - c
        
        # pick non intersecting non unique prefix and suffix
        # can be different sized
        # same characters
        # delete both
        
        # we can use two pointers and 
        # use a conddition where they do not meet

        deq = deque(s)

        l, r = 0 , len(deq) - 1

        while l != r:
            if deq[l] != deq[r]:
                break
            while deq[l] == deq[r]:
                if deq[l] == deq[l+1]:
                    l +=1
                elif deq[r] == deq[r-1]:
                    r -=1
                else:
                    # move both
                    l += 1
                    r -= 1
            for _ in range(l):
                deq.popleft()
            for _ in range(r):
                deq.pop()

            l += 1
            r -= 1

        return len(deq)

    def minimumLength(self, s: str) -> int:
        # Convert string to deque for efficient removal of
        # characters from both ends
        deq = deque(s)

        # Initialize left and right pointers
        l, r = 0, len(deq) - 1

        # While left and right pointers do not meet
        while l < r:
            # If characters at l and r are different, 
            # we can't reduce the string further
            if deq[l] != deq[r]:
                break

            # If characters at l and l+1 are 
            # the same, move l to the right
            while l < r and deq[l] == deq[l + 1]:
                l += 1

            # If characters at r and r-1 are the same, move r to the left
            while l < r and deq[r] == deq[r - 1]:
                r -= 1

            # Move l and r one step inward
            l += 1
            r -= 1

        # Return the length of the remaining string
        return r - l + 1 if l <= r else 0
