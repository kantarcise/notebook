"""
Given a string containing digits from 2-9 inclusive, return 
all possible letter combinations that the number could represent. 

Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is 
given below. 

Note that 1 does not map to any letters.

Example 1:

    Input: digits = "23"
    
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

    Input: digits = ""
    
    Output: []

Example 3:

    Input: digits = "2"
    
    Output: ["a","b","c"]

Constraints:

    0 <= digits.length <= 4
    
    digits[i] is a digit in the range ['2', '9'].

Takeaway:

    If we are deciding on a tree, consider backtracking

    Backtracking is generally recursive. The base case is the end
        recurring is the next step on backtracking and updated path.

    Mapping is clear - hashmap - dicts.
"""

class Solution_:
    def letterCombinations(self, digits):
        # first solution, works and fast too
        ret = []

        if not digits:
            return ret
        
        # map the phone
        # we will be given a string of digits
        phone = {"2":"abc", '3':"def", '4':"ghi", 
                 '5':"jkl", '6':"mno", '7':"pqrs", 
                 '8':"tuv", '9':"wxyz"}

        self.dfs(phone, digits, "", ret)
        return ret
    
    def dfs(self, m, digits, path, ret):
        if not digits:
            ret.append(path)
            return 
        for c in m[digits[0]]:
            self.dfs(m, digits[1:], path+c, ret)

    def letterCombinations_(self, digits):
        # this works too
        
        # solution has to be brute force - backtracking
        # we need some data structure to map the digits
        # at each selection, we decide the choice of the digit we have
        #             .
        #          /  |   \  
        #         a   b    c
        #       /|\  /|\    /|\
        #      def   def    def
        
        # this tree is for "23"
        # ad - ae - af  - bd - be - bf -  ce - cd - cf
        result = []
        phone = {"2" : "abc", "3": "def", "4": "ghi",
                 "5": "jkl", "6": "mno", "7": "qrps",
                 "8": "tuv", "9": "wxyz"}
        def backtrack (i , current_str):
            # THIS IS RECURSIVE
            # WHAT IS THE BASE CASE?
            if len(current_str) == len(digits):
                # we are at the end of the tree.
                # we made all the decisions.
                #  STOP 
                # HAMMERTIME
                result.append(current_str)
                return                
            for c in phone[digits[i]]:
                # recur on backtrack, with next index and updated str
                backtrack(i+1, current_str + c)
        if not digits:
            return []

        backtrack(0, "")
        return result
