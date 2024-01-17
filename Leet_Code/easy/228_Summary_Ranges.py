"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in 
the array exactly. That is, each element of nums is covered by exactly 
one of the ranges, and there is no integer x such that x is 
in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]

Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.

Takeaway:

str(int) is cool way to add items.

Do not forget the last - first item after loop.

Moving the window as you traverse is the key!

"""

class Solution:
    
    def summaryRanges(self, nums: list[int]) -> list[str]:
        # edge case
        if not nums:
            return []
        
        ans = []
        # lets start with what we have
        start = nums[0]
        end = nums[0]
        
        for i in range(1, len(nums)):
            # if the difference is not 1
            if nums[i] != nums[i - 1] + 1:
                # If the difference is not 1, there is 
                # a gap in the sequence.
                
                # If start is equal to end, append the single 
                # element start as a string.
                
                # Otherwise, append the range as a string 
                # in the format '{start}->{end}'.
                ans.append(str(start) if start == end else f'{start}->{end}')
                
                # update the start
                start = nums[i]
            
            # update the end
            end = nums[i]
            
        # there is one more range left behind            
        ans.append(str(start) if start == end else f'{start}->{end}')
        return ans
    
    def summaryRanges_(self, nums: list[int]) -> list[str]:
        """ This did not work,
        Do not forget to move the window as you go!
        """
        result = []
        temp = []
        
        for i in range(1, len(nums)):
            # if the difference is 1 
            if nums[i] - nums[i-1] == 1:
                temp.append(nums[i-1])
            
            # if the difference is 2
            if nums[i] - nums[i-1] == 2:
                if temp:
                    print(temp)
                    result.append(f'"{temp[0]}->{temp[1]}"')
                    temp = []
                result.append([f'"{nums[i]}"'])
        return result
