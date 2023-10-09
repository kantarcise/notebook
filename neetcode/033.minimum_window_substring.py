"""
Given two strings s and t of lengths m and n respectively, return the
 minimum window substring of s such that every character in t (including
  duplicates) is included in the window. If there is no such substring,
return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 
Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?

Takeaway:

Using a hashmap is CLASSIC at this point, for frequency counters in strings

Here are some tips for using the sliding window algorithm to solve problems:

1. Identify the condition that the substring must satisfy. 
This is the most important step, as it will determine how 
the algorithm is implemented.

2. Initialize the sliding window. The sliding window can be 
initialized to be any size, but it is generally a good idea 
to start with a small window and then increase the size of the
 window as needed.

3. Check whether the sliding window satisfies the condition.
This is the core of the sliding window algorithm. If the sliding
window satisfies the condition, then the algorithm has found a
substring that satisfies the condition.

4. Update the sliding window. The sliding window can be updated by 
either incrementing the left pointer or the right pointer.
 Incrementing the left pointer will remove the leftmost character 
 from the window, while incrementing the right pointer will add 
 the next character to the window.

Repeat the process until the end of the string is reached. The 
algorithm should continue to iterate over the string until it reaches
 the end of the string. If the algorithm has not found a substring
that satisfies the condition by the time it reaches the end of
the string, then the algorithm should return an empty string.

"""

class Solution:
    
    # first attempt
    # I could not make it work. I found some strings but not the best strings.
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""

        target_set = set(t)
        possible_results = []
        l = 0

        for r in range(len(t), len(s)):
            # increase left pointer where the set is not enough
            temp_set = set(s[l:r])
            if (temp_set & target_set == target_set):
                possible_results.append([s[l:r], len(s[l:r])])
                l += 1
            # increase right pointer where there is no chance

        return min(possible_results, key = lambda a: a[1])[0]


    def min_window(self, s: str, t: str) -> str:
        
        # this approach uses hashmaps
        # for target as well as window
        # target is what we need
        # window is what we have

        # our condition for returning the window will be
        # "have" dictionary having more or equal than "need" dictionary
        # for every character in those dictionaries

        if t == "": return ""

        count_t, window = {}, {}

        # make every letter in t the keys of the target dictionary
        for char in t:
            count_t[char] = 1 + count_t.get(char, 0) 

        # in the start, we have nothing so have is zero. 
        # we need at least length of the target string
        have, need = 0 , len(count_t) 

        # at start the window could be just -1 to -1 with infinite length
        # we are trying to find the shortest substring with indexes stored in result_indexes
        result_indexes, result_length = [-1, -1], float("infinity")

        # setup sliding window
        l = 0
        for r in range(len(s)):

            # add the new character to window
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # this character is useful!
            if c in count_t and window[c] == count_t[c]:
                have +=1
            
            # if we got a possible result, increment left pointer on condition 
            while have == need:
                # update the result_indexes, found a shorter string
                if (r - l + 1) < result_length:
                    result_indexes = [l, r]
                    result_length = (r - l + 1)
                
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        
        l, r = result_indexes
        return s[l:r+1] if result_length != float("infinity") else ""


if __name__ == "__main__":
    sol = Solution()

    # did not work
    # print(sol.minWindow(s = "ADOBECODEBANC", t = "ABC"))
    # print(sol.minWindow(s = "a", t = "a"))
    # print(sol.minWindow(s = "a", t = "aa"))

    print(sol.min_window(s = "ADOBECODEBANC", t = "ABC"))
    print(sol.min_window(s = "a", t = "a"))
    print(sol.min_window(s = "a", t = "aa"))
