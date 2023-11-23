"""
You are given an array of characters letters that is sorted in non-decreasing 
order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater 
than target. If such a character does not exist, return the first character in letters.

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
 

Constraints:

2 <= letters.length <= 104
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.

Takeaway:

You clearly see the list in non deacreasing order. 
You gotta think of binary search.

You dont have to return the middle index immediately after you found it!

"""

class Solution:
    def nextGreatestLetter_(self, letters: List[str], target: str) -> str:
        # we have a list of strings with at least 2 different characters

        # this solution gives an error:
        
        low, high = 0, len(letters) -1
      
        while low <= high:
            middle = low + ((high - low) // 2)
            if target == letters[middle]:
                return letters[middle + 1] if target != letters[middle+1] else letters[middle + 2]
            elif target < letters[middle]:
                high = middle - 1
            else:
                low = middle + 1
        return letters[0]
        
        # my first approach was basic traversal - linear time
        
        # if ord(target) >= ord(letters[-1]):
        #     return letters[0]
        # for elem in letters:
        #     if ord(elem) > ord(target):
        #         return elem

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # binary search approach 
        l, r = 0, len(letters) - 1
        while l <= r:
            mid = (l + r) // 2
            if letters[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        if l < len(letters):
            return letters[l]
        else:
            return letters[0]
