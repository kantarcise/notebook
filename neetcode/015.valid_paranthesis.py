"""
Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine 
if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Constraints:

   1 <= s.length <= 10^4
   s consists of parentheses only '()[]{}'.

# Takeaway

   - matching symbols is just asking for a hash map to be used

   - we are using a stack for storing all of the opening brackets.

   - For each closing bracket we are looking for the last element 
   - in stack to be matched by the closing symbol

   - if everything went smooth, stack should be empty in the end.

"""

class Solution:
    def isValid(self, s: str) -> bool:
        # we can use a dictionary for matched characters:

        match = {"(": ")",
                 "{": "}",
                 "[": "]"}
        
        # use a list for the stack
        stack = []

        for c in s:
            if c in match:
                stack.append(c)
            elif c in ")]}":
                if len(stack) == 0 or match[stack[-1]] != c:
                    # if nothing to pop, not valid
                    # if top of stack does not match the expected, not valid
                    return False
                stack.pop()

        # if stack is empty in the end, all matched
        return not bool(stack)
    
    def is_valid_(self, s: str) -> bool:
        # we can use a dictionary for matched characters:
        matching_symbols = { ')': '(',
                             ']': '[',
                             '}': '{'  }
            
        _stack = []
        
        for symbol in s:
            if symbol in "([{":
                _stack.append(symbol)
            elif symbol in ")]}":
                if len(_stack) == 0 or _stack[-1] != matching_symbols[symbol]:
                    return False
                _stack.pop()
                
        return len(_stack) ==  0

    def is_valid_improved(self, s: str) -> bool:
        matching_symbols = { ')': '(',
                             ']': '[',
                             '}': '{'  }
            
        _stack = []

        opening_brackets = {"(", "[", "{"}
        closing_brackets = {")", "]", "}"}
        
        for symbol in s:
            if symbol in opening_brackets:
                _stack.append(symbol)
            elif symbol in closing_brackets:
                # we can use the boolean for a sequence
                # last element should be closed asap.
                if not _stack or _stack[-1] != matching_symbols[symbol]:
                    return False
                _stack.pop()
                
        return len(_stack) ==  0
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.is_valid("()"))
    print(sol.is_valid("()[]{}"))
    print(sol.is_valid("()[]{}"))
    print(sol.is_valid("(]"))
    print(sol.is_valid_("()"))
    print(sol.is_valid_("()[]{}"))
    print(sol.is_valid_("()[]{}"))
    print(sol.is_valid_("(]"))
    print(sol.is_valid_improved("()"))
    print(sol.is_valid_improved("()[]{}"))
    print(sol.is_valid_improved("()[]{}"))
    print(sol.is_valid_improved("(]"))
