"""
Given a 1-indexed array of integers numbers that is already sorted 
in non-decreasing order, find two numbers such that they add 
up to a specific target number. 

Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added 
by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. 

You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    
    Explanation: The sum of 2 and 7 is 9. 
      Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

    Input: numbers = [2,3,4], target = 6
    Output: [1,3]
    
    Explanation: The sum of 2 and 4 is 6. 
      Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

    Input: numbers = [-1,0], target = -1
    Output: [1,2]
    
    Explanation: The sum of -1 and 0 is -1. 
      Therefore index1 = 1, index2 = 2. We return [1, 2].
 
Constraints:

    2 <= numbers.length <= 3 * 10^4
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    The tests are generated such that there is exactly one solution.

Takeaway:

    Enumerate is still one of the best ways to 
      traverse a sequence.

    You can and you should use dicts whenever you want to store 
      and access a value/key combination.
"""
class Solution():

    def twoSum(self, numbers: list, target: int) -> list:
        # input is sorted.
        
        # We can use two pointers to approach our target!
        
        l, r = 0, len(numbers)-1
        
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                # we found the target!
                # because input is 1 indexed, we add 1
                return [l+1, r+1]
            elif s < target:
                # we need a bigger left value
                l += 1
            else:
                # we need a smaller right value
                r -= 1

    def twoSum_(self, numbers: list, target: int) -> list:
        # input is sorted.
        
        # when input is sorted what do we think of?
        # Binary Search!

        # using constant extra space !
        # time complexity is O(nlogn)

        for i in range(len(numbers)):
            
            l, r = i+1, len(numbers)-1
            complement = target - numbers[i]
            while l <= r:
                mid = l + ((r-l) // 2)
                if numbers[mid] == complement:
                    return [i+1, mid+1]
                elif numbers[mid] < complement:
                    l = mid+1
                else:
                    r = mid-1

    def twoSum__(self, numbers: list, target: int) -> list:
        # a simple approach would be to use a dictionary
        # but that would not be constant space.

        # here is just for practice
        
        numbers_to_index = {}
        for index, number in enumerate(numbers):
            # find the complement
            complement = target - number

            if complement in numbers_to_index:
                # we found the complement!
                # add 1 to indexes
                return [numbers_to_index[complement] + 1, index + 1]
            # else
            # just add this number to the dictionary
            numbers_to_index[number] = index

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], target = 9))
    print(sol.twoSum([5,25,75], target = 100))
    print(sol.twoSum_([2,7,11,15], target = 9))
    print(sol.twoSum_([5,25,75], target = 100))
    print(sol.twoSum__([2,7,11,15], target = 9))
    print(sol.twoSum__([5,25,75], target = 100))
