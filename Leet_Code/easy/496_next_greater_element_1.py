"""

The next greater element of some element x in an array is the first 
greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, 
where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] 
and determine the next greater element of nums2[j] in nums2. If there is 
no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is 
the next greater element as described above.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 
Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
 
Follow up: Could you find an O(nums1.length + nums2.length) solution?

Takeaway:

you can simply make a mapping for greater elements in a list, with a help of a stack


"""

class Solution:
    def nextGreaterElement_(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # myt first approach
        # did not work  
      
        # did not ask the question to myself, should I use a hashmap?
        # should I use heap? a STACK maybe?
        
        # nums 1 is subset of nums2
        # len(nums1) traverse
        
        result = [0] * len(nums1) 
        for index, element in enumerate(nums1):
            # find the index for nums2 - j
            j = nums2.index(element)  
            # look to the right of j for greater element
            if j == (len(nums2) - 1):
                result[index] = -1
            while j < (len(nums2) - 1):
                if nums2[j+1] > element:
                    result[index] = nums2[j+1]
                    j += 1
                else:
                    j += 1
                if j == (len(nums2) - 1):
                    result[index] = -1
                    break
        return result
    
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # example case:
        # Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
        # Output: [-1,3,-1]
      
        # the result is a list with same length as nums1
        result = []
        stack = []
        mapping = {}

        # This loop iterates through each element n in nums2. It checks if 
        # n is greater than the element at the top of the stack (stack[-1]). 
        # If it is, it means n is the next greater element for the element at the top of
        # the stack. We pop elements from the stack and update the mapping dictionary 
        # accordingly. This process continues until the stack is empty or the top 
        # element is less than or equal to n. Finally, n is pushed onto the stack.
        for n in nums2:
            while stack and n > stack[-1]:
                mapping[stack.pop()] = n
            stack.append(n)

        # After the loop, if there are elements left in the stack, it means 
        # there is no next greater element for these elements in nums2. For each 
        # remaining element in the stack, we set its next greater element to -1.
        while stack:
            mapping[stack.pop()] = -1

        # now we have the mapping for nums2.
        for n in nums1:
            result.append(mapping[n])

        return result

  
