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

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.


Takeaway:

Binary search, whether implemented iteratively or recursively, has a 
time complexity of O(log n) because it continuously reduces the search
 range by half with each comparison. This logarithmic time complexity
  is significantly faster than linear time complexity (O(n)), especially
   for large lists.

In basic search, you can traverse the sequence but that would be O(n).
We use 2 pointers and check if target is equal to kinda middle of the 
sequence so that we eliminate more than one value each loop. 

"""


class Solution:


    def search_recursive(self, nums, target):
        """
        Perform binary search recursively to find the target in a sorted list.

        :param nums: A sorted list of integers.
        :param target: The target integer to search for.
        :return: The index of the target if found, or -1 if not found.
        """
        return self._binary_search_recursive(nums, target, 0, len(nums) - 1)

    def _binary_search_recursive(self, nums, target, left, right):
        
        if left > right :
            return -1 # target not found

        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            return self._binary_search_recursive(nums, target, mid+1, right )

        else:
            return self._binary_search_recursive(nums, target, left, mid - 1)

    def search_iterative(self, nums, target):
        
        low, high = 0, len(nums) - 1

        while low <= high:
            
            # in Python no problem because integers are unbounded
            # if low is close to 2^31 addition might cause error
            # this might overflow in other languages
            # mid = (low + high) // 2 

            # here is a better way:
            # calculating midway without adding them together
            # low + (half of the distance between low and high)
            mid = low - ((high - low) // 2)
            
            if target == nums[mid]:
                return mid

            elif target < nums[mid]:
                high = mid - 1 # only left values

            else: 
                low = mid + 1 # only right values

        return -1 # could not be found


    def search_iterative_(self, nums, target):
        
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + ((high - low) // 2)

            if target == nums[mid]:
                return mid

            elif target < nums[mid]:
                high = mid - 1 # only left values
            
            else:
                low = mid + 1 # only right values

        return -1 # could not be found


if __name__ == "__main__":
    sol = Solution()

    print(sol.search_recursive([-1,0,3,5,9,12], 9))
    print(sol.search_recursive([-1,0,3,5,9,12], 2))

    print(sol.search_iterative([-1,0,3,5,9,12], 9))
    print(sol.search_iterative([-1,0,3,5,9,12], 2))

