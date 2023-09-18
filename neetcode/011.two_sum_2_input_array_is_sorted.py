"""

Given a 1-indexed array of integers numbers that is already sorted in non
-decreasing order, find two numbers such that they add up to a specific 
target number. Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one
 as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may
 not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.


Takeaway:

enumerate is still one of the best ways to traverse a sequence.

YOu can and you should use dictinaries whenever you want to store 
and access a value/key combination.


"""


class Solution():

    # my first try, not bad. SOlid pseudo code.
    def two_sum(self, seq, target):
        # write a single loop that iterates over the sequence, 
        # with two different pointers to the sequence
        # if you have the target result, result both indexes
        
        small_index = 0
        for big_index, elem in enumerate(seq):
            if elem + seq[small_index] == target and small_index != big_index:
                return [small_index + 1, big_index + 1]
            if big_index == len(seq) - 1:
                small_index +=1
            
    def twoSum(self, numbers, target):
        # we can use an dictionary to store indexes of elements
        num_to_index = {}
        for index, num in enumerate(numbers):
            # what are we looking for to get the result?
            complement = target - num
            # if we have it in the sequence
            if complement in num_to_index:
                # return the index of the complement from the dict, and 
                # the index of the element we are currently at.
                return [num_to_index[complement] + 1, index + 1]
            # if we dont have it in the sequence
            # add it to the dictionary with its index
            num_to_index[num] = index


    def twoSumMine(self, seq, target):
        numbers_to_index = {}
        for index, number in enumerate(seq):
            complement = target - number
            if complement in numbers_to_index:
                return [numbers_to_index[complement] + 1, index + 1]
            # else
            numbers_to_index[number] = index



if __name__ == "__main__":
    sol = Solution()
    print(sol.two_sum([2,7,11,15], target = 9))
    print(sol.two_sum([5,25,75], target = 100))
    print(sol.twoSum([2,7,11,15], target = 9))
    print(sol.twoSum([5,25,75], target = 100))
    print(sol.twoSumMine([2,7,11,15], target = 9))
    print(sol.twoSumMine([5,25,75], target = 100))
