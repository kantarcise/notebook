"""
There is an integer array nums sorted in ascending order (with 
distinct values).

Prior to being passed to your function, nums is possibly 
rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is 

[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] 

(0-indexed). 
  
For example, [0,1,2,4,5,6,7] might be rotated at pivot 
index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
 
Example 1:

    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

Example 3:

    Input: nums = [1], target = 0
    Output: -1
 

Constraints:

    1 <= nums.length <= 5000
    -10^4 <= nums[i] <= 10^4
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -10^4 <= target <= 10^4

Takeaway:

    Any time you are looking for a log time complexity, you should look for binary search.

    For this question, it's like we have 2 sorted sequences combined.

    Look  at the picture before writing the code. Give 2 discrete 
        examples for different edge cases.

"""

class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while  l <= r:
            
            # the usual
            mid = l + ((r - l) // 2)

            # base case
            if nums[mid] == target:
                return mid

            # if left pointer is smaller than middle
            # middle value belongs to left sorted portion.
            if nums[l] <= nums[mid]:
                # Left half is sorted
                if nums[l] <= target < nums[mid]:
                    # shrink to left, move right pointer.
                    r = mid - 1
                else:
                    l = mid + 1
            
            # middle value belongs to right sorted portion
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


if __name__ == '__main__':
    sol = Solution()

    print(sol.search(nums = [4,5,6,7,0,1,2], target = 0)) # 4
    print(sol.search(nums = [4,5,6,7,0,1,2], target = 3)) # -1
    print(sol.search( nums = [1], target = 0)) # -1
