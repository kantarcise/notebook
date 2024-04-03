"""
Given an array of integers nums which is sorted in ascending
order, and an integer target, write a function to search
target in nums. If target exists, then return its index. 

Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4

    Explanation: 9 exists in nums and its index is 4

Example 2:

    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1

    Explanation: 2 does not exist in nums so return -1
 
Constraints:

    1 <= nums.length <= 10^4
    -10^4 < nums[i], target < 10^4
    All the integers in nums are unique.
    nums is sorted in ascending order.

Takeaway:

Binary search, whether implemented iteratively or recursively, has a 
time complexity of O(log n) because it continuously reduces the search
range by half with each comparison. 

This logarithmic time complexity is significantly faster than 
linear time complexity (O(n)), especially for large lists.

In basic search, you can traverse the sequence but that would be O(n).
We use 2 pointers and check if target is equal to kinda middle of the 
sequence so that we eliminate more than one value each loop. 

"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            middle = (low + (high - low) // 2)
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1

        return -1 

    def search_(self, nums: list[int], target: int) -> int:
        """
        We can solve this problem recursively too.
        """
        return self._binary_search_recursive(nums, target, 0, len(nums) - 1)

    def _binary_search_recursive(self, nums, target, left, right):
        
        if left > right :
            return -1 # target not found

        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            return self._binary_search_recursive(nums, target, mid+1, right)

        else:
            return self._binary_search_recursive(nums, target, left, mid - 1)


if __name__ == "__main__":
    sol = Solution()

    print(sol.search([-1,0,3,5,9,12], 9))
    print(sol.search([-1,0,3,5,9,12], 2))

    print(sol.search_([-1,0,3,5,9,12], 9))
    print(sol.search_([-1,0,3,5,9,12], 2))
