"""

Given two strings s1 and s2, return true if s2 contains a permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.


Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true

Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 
Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

Takeaway: 

# do not forget about edge cases.

# string character frequency is a GREAT usecase for Hashmaps

comparing a sliding window for the target string can be an approach

[1, 2, 3] != [3, 2, 1] - so use dictionaries

"""

class Solution:
    
    # my approach
    # low memory usage but slow code.
    def checkInclusion(self, s1, s2) -> bool:
        # eidbaooo  - ab
        # we are looking for a window which has the same size as s1
        l, r = 0 , len(s1)

        s1_dict = {}
        for char in s1:
            # if it already exists, add 1 to value
            s1_dict[char] = s1_dict.get(char, 0 ) + 1

        while r <= len(s2):
            temp_dict = {}
            for char in s2[l:r]:
                temp_dict[char] = temp_dict.get(char, 0) + 1
            if s1_dict == temp_dict:
                return True
            l += 1
            r += 1
            del temp_dict
            
        return False

    # using big hashmaps for all language,
    # checking the count of hashes
    def check_inclusion_faster(self, s1, s2) -> bool:
        
        # check if the length of s1 is greater than the length of s2. If it is, 
        # then you can immediately return False because s2 
        # cannot contain a permutation of s1.
        if len(s1) > len(s2) : return False
        
        # character counts for s1 and s2
        s1_count, s2_count = [0] * 26 , [0] * 26

        # iterate over s1
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # calculate the number of matches between s1_count and s2_count
        matches = 0
        for i in range(26):
            matches += (1 if s1_count[i] == s2_count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            # if matches is 26, there is a permutation
            if matches == 26: return True

            index = ord(s2[r]) - ord("a")
            s2_count[index] += 1

            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")

            s2_count[index] -= 1

            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1

            l += 1
        
        return matches == 26




if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion(s1 = "ab", s2 = "eidbaooo"))
    print(sol.checkInclusion( s1 = "ab", s2 = "eidboaoo"))
    print(sol.checkInclusion( s1 = "hello", s2 = "ooolleoooleh"))

    print(sol.check_inclusion_faster(s1 = "ab", s2 = "eidbaooo"))
    print(sol.check_inclusion_faster( s1 = "ab", s2 = "eidboaoo"))
    print(sol.check_inclusion_faster( s1 = "hello", s2 = "ooolleoooleh"))