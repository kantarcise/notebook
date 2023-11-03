"""
Given a string s, partition s such that every
substring
of the partition is a
palindrome
. Return all possible palindrome partitioning of s.

 
Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]

Constraints:

    1 <= s.length <= 16
    s contains only lowercase English letters.

Takeaway:

Palindrome is just a string - racecar

Partitioning

    [aabb]
    /   \
   aa    bb

root is the string
nodes are different choices
think just like a labyrthn. 
 
Still need work on backtracking.
"""

class Solution_:

    # my first approach, 
    # I am acting like I dont know backtracking
    # which might be the case.
    def partition_(self, s: str) -> "list[list[str]]":
        # palindrome is racecar
        # every single string is viable
        result = []
        
        # single partitioning, always
        temp = [elem for elem in s]
        result.append(temp)
        
        def is_palindrome(seq):
            return seq == seq[::-1]
        # based on the size of the string
        
        # we need to check 2s
        # than 3s
        # than 4s
        
        string_size = 2
        
        while string_size <= len(s):
            temp = []
            for i in range(len(s)):
                try:
                    if is_palindrome(s[i:i+string_size]):
                        temp.append(s[i:i+string_size])
                except:
                    pass
            result.append(temp)
            string_size += 1
            
        return result

class Solution:

    def partition(self, s: str) -> "list[list[str]]":
        # neetcode
        # we will use backtracking

        # root is the string
        # nodes are different choices
        # think just like a labyrthn. 

        res = []
        partition = []

        def dfs(i):
            if i >= len(s):
                # we made it to the end    
                res.append(partition.copy())
                return
            
            # if we have not reached the last index
            for j in range(i, len(s)):
                # i and j are left and right boundaries
                if self.is_palindrome(s, i , j):
                    partition.append(s[i:j+1])
                    # now we can start to look for the next
                    # palindrome
                    dfs(j + 1)
                    # after looking of all additional partitions
                    # we can pop what we added
                    partition.pop()

        # 0 is the starting index
        dfs(0)
        return res

    def is_palindrome(self, s, l, r):
        # return True if s is a plaindrome 
        # starting at index l and ending at r
        while l < r:
            if s[l] != s[r]:
                return False
            l , r  = l + 1 , r - 1
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.partition("aab"))