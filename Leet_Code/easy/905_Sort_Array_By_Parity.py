"""
Given an integer array nums, move all the even integers 
at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:

Input: nums = [0]
Output: [0]

Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000

Takeaway:

extend and append. Can we do this O(1) memory ?

"""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result_even = []
        result_odd = []
        for elem in nums:
            if elem % 2 == 0:
                result_even.append(elem)
            else:
                result_odd.append(elem)
                
        result_even.extend(result_odd)
        
        return result_even
