"""
Suppose an array of length n sorted in ascending order 
is rotated between 1 and n times. 

For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.

    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array 

    [a[0], a[1], a[2], ..., a[n-1]] 

1 time results in the array 

    [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, 
return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:

    Input: nums = [3,4,5,1,2]
    Output: 1
    Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:

    s: nums = [4,5,6,7,0,1,2]
    Output: 0
    Explanation: The original array was [0,1,2,4,5,6,7] and 
        it was rotated 4 times.

Example 3:

    Input: nums = [11,13,15,17]
    Output: 11
    Explanation: The original array was [11,13,15,17] and it 
        was rotated 4 times. 

Constraints:

    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    All the integers of nums are unique.
    nums is sorted and rotated between 1 and n times.

Takeaway:

    If you see a O(log n) in the question, instantly think 
        of binary search.

    Because we know the sequence is sorted, rotated but sorted, 
        we can use this to our advantage.

    If the mid we calculate is bigger than left pointer, then 
        we are in the sorted part of left, so go to the right.

    If the mid we calculate is smaller than right pointer, than 
        we are in the sorted part of right, so go to the left 
        for even smaller numbers.

"""

class Solution:
    def findMin__(self, nums: list[int]) -> int:
        # this is o(n)
        # LOL
        return min(nums)

    def findMin_(self, nums: list[int]) -> int:

        # [3, 4, 5, 1, 2] -  min is 1  - 1 is at index 3

        left, right = 0, len(nums) - 1

        # left and right both converge to the minimum index;
        while left < right:

            mid = left + ((right - left) // 2)

            # In normal binary search, we have a target 
            # to match exactly,
            # We would have a specific branch for if nums[mid] == target.
            # we do not have a specific target here, so we just have simple if/else.

            # the main idea for our checks is to converge the 
            # left and right bounds on the start of the pivot,
            # and never disqualify the index for a possible minimum value.

            if nums[mid] > nums[right]:
                
                # if this is True, then we know that in the 
                # middle of the sequence, there is a bigger value than at its left.

                # we are focused on the bigger part
                left = mid + 1
            else:
                # if it is not True, that means that in the middle of the sequence
                # there is a smaller value than at its left
                
                # we should focus on the smaller part
                right = mid

        # left and right both getting closer to the minimum value

        # when left bound increases, it does not disqualify a value that could 
        # be smaller than something else (we know nums[mid] > nums[right])
        
        # So nums[right] wins and we ignore mid and everything to the left of mid.

        # when right bound decreases, it also does not disqualify a
        # value that could be smaller than something else 
        # We know nums[mid] <= nums[right], so nums[mid] wins and we keep it for now.

        # We shrink the left/right bounds to one value,
        # without ever disqualifying a possible minimum
        return nums[left]

    def findMin(self, nums: list[int]) -> int:
        # can be any value at start.
        res = nums[0]

        l, r = 0 , len(nums) - 1

        while l <= r:
            
            # if we arrive at a sorted sequence,
            if nums[l] < nums[r]:
                # we can simply return the leftmost value
                res = min (res, nums[l])
                break

            # not sorted, binary search at the start.
            m = l + ((r - l) // 2)

            # potential result
            res = min(res, nums[m])
            
            # is this mid value greater than left?
            if nums[m] >= nums[l]:
                # if it is, look at the right side of the sequence
                l = m + 1
            else:
                # if not, look at the left side of the sequnce
                r = m - 1
        return res

if __name__ == '__main__':
    sol = Solution()

    print(sol.findMin([3,4,5,1,2]))
    print(sol.findMin([4,5,6,7,0,1,2]))
    print(sol.findMin([11,13,15,17]))

    print(sol.findMin_([3,4,5,1,2]))
    print(sol.findMin_([4,5,6,7,0,1,2]))
    print(sol.findMin_([11,13,15,17]))

    print(sol.findMin__([3,4,5,1,2]))
    print(sol.findMin__([4,5,6,7,0,1,2]))
    print(sol.findMin__([11,13,15,17]))
