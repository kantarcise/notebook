"""
You are given an array of strings arr. A string s is formed 
by the concatenation of a subsequence of arr that 
has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array 
by deleting some or no elements without changing the order of 
the remaining elements.

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are 
            "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
 
Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.

Takeaway:

Backtracking!
"""

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # arr = ["cha","r","act","ers"]
        def backtrack(start, current):
            # max length currently
            max_length = len(current)
            # for every starting element in arr 
            for i in range(start, len(arr)):
                # Check string is unique or not, if unique, keep combining further
                if len(current + arr[i]) == len(set(current + arr[i])):
                    # unique, possibly update the max len
                    max_length = max(max_length, backtrack(i + 1, current + arr[i])) 
                    
            return max_length

        return backtrack(0, "") #Start with an empty string

# Example
# Suppose we have strings ["ab", "cd", "a"].

# Start with "ab". It's unique, so consider it.
# Add "cd". Now you have "abcd", which is still unique.
# Try to add "a". But "abcd" + "a" is not unique (it has two 'a's), so you don't consider this combination.
# The longest unique combination here is "abcd" with a length of 4.
