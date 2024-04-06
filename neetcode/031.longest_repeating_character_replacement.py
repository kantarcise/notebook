"""
You are given a string s and an integer k. 

You can choose any character of the string and change it to 
any other uppercase English character. 

You can perform this operation at most k times.

Return the length of the longest substring containing the same 
letter you can get after performing the above operations.
 

Example 1:

    Input: s = "ABAB", k = 2
    Output: 4

    Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

    Input: s = "AABABBA", k = 1
    Output: 4

    Explanation: 
        
        Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    
        The substring "BBBB" has the longest repeating letters, which is 4.
    
        There may exists other ways to achive this answer too.
 
Constraints:

    1 <= s.length <= 10^5
    s consists of only uppercase English letters.
    0 <= k <= s.length

Takeaway:

    For a string,  we need to remember that there are 26 letters in 
    the English language

    we want to maximize the number of characters in the substring 
    to get to the max number of characters, we would want to replace 
    the characters that occurs the least. (less frequent)

    We need to setup a sliding window that changes its size based on the
    number of characters we can replace (k) and the equation we know.

    for every substring, we can calculate the characters to be replaced by:
    ```windowLen - count[mostFrequent]  <= k```
    where count is a dictionary (hash map) with occurences of characters

"""

class Solution:
    
    def characterReplacement__(self, s, k ) -> int:
        # does not work

        # seq = "sezai" , k = 2
        # becuase we can change k characters in the string.
        # we need longest substrings with same characters 
        # containing at most k different characters
        
        l = 0 
        character_set = set()

        for r in range(len(s)):
            if s[r] in character_set:
                character_set.remove(s[l])
                l += 1
            character_set.add(s[r])
        
        pass

    def characterReplacement_(self, s, k ) -> int:
        # there are 26 uppercase characters in English language
        # we want to maximize the number of characters in the substring
        # to get to the max number of characters, we would want to replace 
        # the characters that occurs the least. (less frequent)

        # AAAABAB
        # for example B here

        # for every substring, we can calculate the characters to be replaced by:
        # windowLen - count[mostFrequent]  <= k
        # where count is a dictionary (hash map) with occurences of characters

        # we need to setup a sliding window that changes its size based on the
        #  number of characters we can replace (k) and the equation we know.

        count_occurences = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count_occurences[s[r]] = 1 + count_occurences.get(s[r], 0)

            while (r - l + 1) - max(count_occurences.values()) > k:
                # increment the left pointer, we cannot use this window
                count_occurences[s[l]] -= 1
                l += 1 

            res = max(res, r - l + 1)
            
        return res


    def characterReplacement(self, s, k ) -> int:
        # we dont have to update the max frequency
        # check neet code for explanation

        count_occurences = {}
        res = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):
            count_occurences[s[r]] = 1 + count_occurences.get(s[r], 0)
            max_freq = max(max_freq, count_occurences[s[r]])
            while (r - l + 1) - max_freq > k:
                # increment the left pointer, we cannot use this window
                count_occurences[s[l]] -= 1
                l += 1 

            res = max(res, r - l + 1)
            
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement_(s = "AABABBA", k = 1))
    print(sol.characterReplacement_("ABAB", k = 2))

    print(sol.characterReplacement(s = "AABABBA", k = 1))
    print(sol.characterReplacement("ABAB", k = 2))
