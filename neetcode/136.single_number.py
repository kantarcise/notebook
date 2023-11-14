"""
Given a non-empty array of integers nums, every 
element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime 
complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104

Each element in the array appears twice except for one 
element which appears only once.

Takeaway:

IF we had no mem constraint, we could've used a hash set
and added every element to it and removed if encountered again
the remaining element would be the solution

how can you figure this out?
write the numbers in binary:

 [4, ->  100 
  1, ->  001
  2, ->  010
  1, ->  001
  2  ->  010
  ]

how can we get rid of the numbers that 
are occuring twice?

XOR ! 

xor is apple
if you are different, you are 1
if you are same, you are 0

Any number XOR'ed with 0 
remains unchanged. a ^ 0  = a.

how?

Because every 0 would stay 0 when its XORed with 0s
every 1 would be 1 when it is XORed with 0s


"""

class Solution:

    # bitwise operator solution
    def singleNumber(self, nums: list[int]) -> int:
        

        # how can you figure this out?
        # write the numbers in binary:

        #  [4, ->  100 
        #   1, ->  001
        #   2, ->  010
        #   1, ->  001
        #   2  ->  010
        #   ]

        # how can we get rid of the numbers that 
        # are occuring twice?

        # XOR ! 

        # xor is apple
        # if you are different, you are 1
        # if you are same, you are 0

        # Any number XOR'ed with 0 
        # remains unchanged. a ^ 0  = a.

        # how?

        # Because every 0 would stay 0 when its XORed with 0s
        # every 1 would be 1 when it is XORed with 0s

        result = 0 # because - a ^ 0  = a
        for elem in nums:
            result ^= elem
        return result