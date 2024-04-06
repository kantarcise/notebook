"""
Given a string s, find the length of the longest substring 
without repeating characters.

Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.

    Notice that the answer must be a substring, "pwke" is a 
    subsequence and not a substring. 

Constraints:

    0 <= s.length <= 5 * 10^4
    s consists of English letters, digits, symbols and spaces.


Takeaway:

    Sets are great for duplicate questions

    For a sliding window, you still need to have two pointers

    With thinking about the worst case, you can set 
    up conditions around it.

"""

class Solution:

    def lengthOfLongestSubstring__(self, s) -> int:
        # does not work

        # abcabcbb
        # iterate over ever element,
        # if ther are not equal to one after them
        # add it to a list of lists

        result = [[]]
        
        l, r = 0, 1

        while r < len(s):
            counter = 0
            
            if len(result) == 0:
                result[counter].append(s[l])
                l += 1 

            elif s[l] not in result[counter]:
                result[counter].append(s[l])
                r += 1
                l += 1
            else:
                pass
        
        pass

    def lengthOfLongestSubstring(self, s) -> int:
        # a classic sliding window question
        # we can use a set and only traverse over sequence once
        # so we will get o(n) complexity
        # we will be adding and removing from our set.
        # we should also keep the longest substring length.

        character_set = set()

        result = 0

        # fowr the sliding window, we will be needing two pointers
        l  = 0
        # right pointer will be changing
        for r in range(len(s)):
            # if the next character we see is already inside the set
            while s[r] in character_set:
                # remove the duplicate from the set    
                character_set.remove(s[l])
                # move l up
                l += 1
            # if we have a new character
            character_set.add(s[r])
            result = max(result , r - l + 1)
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb")) # 3
    print(sol.lengthOfLongestSubstring("bbbbb")) # 1
    print(sol.lengthOfLongestSubstring("pwwkew")) # 3

