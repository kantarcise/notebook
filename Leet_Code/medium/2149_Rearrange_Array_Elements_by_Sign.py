"""
You are given a 0-indexed integer array nums of 
even length consisting of an equal number of positive 
and negative integers.

You should rearrange the elements of nums such that 
the modified array follows the given conditions:

Every consecutive pair of integers have opposite signs.

For all integers with the same sign, the order 
in which they were present in nums is preserved.

The rearranged array begins with a positive integer.

Return the modified array after rearranging the 
elements to satisfy the aforementioned conditions.

Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]

Explanation:
The positive integers in nums are [3,1,2]. 
The negative integers are [-2,-5,-4].

The only possible way to rearrange them such that 
they satisfy all conditions is [3,-2,1,-5,2,-4].

Other ways such as [1,-2,2,-5,3,-4], 
                   [3,1,2,-2,-5,-4], 
                   [-2,3,-5,1,-4,2] are incorrect 
      because they do not satisfy one or more conditions.  

Example 2:

Input: nums = [-1,1]
Output: [1,-1]

Explanation:

1 is the only positive integer and -1 the only 
negative integer in nums.

So nums is rearranged to [1,-1].
 
Constraints:

  2 <= nums.length <= 2 * 105
  nums.length is even
  1 <= |nums[i]| <= 105
  nums has equal number of positive and negative integers.

Takeaway:

You can use 2 lists and append acoordingly

Or you can use two pointers which is more elegant.
"""
class Solution:
    def rearrangeArray_(self, nums: List[int]) -> List[int]:
        # can we make signed lists?
        # yes we can!
        pos, neg = [], []
        
        for elem in nums:
            if elem >= 1:
                pos.append(elem)
            else:
                neg.append(elem)
            
        res = []
        for i in range(len(nums)//2):
            res.append(pos[i])
            res.append(neg[i])
            
        return res
    
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # two pointers
        # start from 0 and 1        

        
        ans = [0] * len(nums)
        pos, neg = 0, 1
        
        for num in nums:
            if num > 0:
                ans[pos] = num
                # next positive will be next 
                # to the next index
                pos += 2
            else:
                ans[neg] = num
                # same way
                neg += 2
        
        return ans
