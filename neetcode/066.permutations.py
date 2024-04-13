"""
Given an array nums of distinct integers, return all the 
possible permutations. 

You can return the answer in any order.

Example 1:

    Input: nums = [1,2,3]
    
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

    Input: nums = [0,1]
    
    Output: [[0,1],[1,0]]

Example 3:

    Input: nums = [1]
    
    Output: [[1]] 

Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.

Takeaway:

    There is itertools for permutation and combination

    You can use a stack with recursion

    You can use backtracking, thinking with a decision tree

    pop an element and call permute again on the smaller sequence

    before returning to the beginning of the loop, 
    append back the element you popped
    This way, you'll traverse the sequence exactly how you want.

"""

from itertools import permutations

class Solution:
    
    def permute__(self, nums: "list[int]") -> "list[list[int]]":
        
        # first try
        # [0, 1]
        # [1, 0], [0, 1]
        # how do we make permutations
        # we select a element, than another element, than another.
        # we make sure our selection is unique

        # we have this wonderful tool
        perms = permutations(nums, len(nums))
        # print ("".join(perms) for perm in perms)
        return [i for i in perms]

    def permute_(self, nums: "list[int]") -> "list[list[int]]":
        # a non recursive appproach with a stack

        # Initialize the stack with individual elements
        stack = [[i] for i in nums]  
        # stack =  [[0], [1], [2]]
        permutations = []  # List to store the final permutations
    
        while stack:
            # Pop the current partial permutation from the stack
            current_permutation = stack.pop()  
    
            if len(current_permutation) == len(nums):
                # A permutation of length n is complete
                #  add it to the list of permutations
                permutations.append(current_permutation)
            else:
                # Continue building the permutation by 
                # adding unused elements to the end
                unused_elements = [elem for elem in nums if 
                                        elem not in current_permutation]
                for elem in unused_elements:
                    stack.append(current_permutation + [elem])
    
        return permutations

    def permute(self, nums: "list[int]") -> "list[list[int]]":
        
        # we can think of the problem as a decision tree
        #                     [1,2,3] 
        #   [2,3]              [1,3]               [1,2]
        # [3]  [2]            [3]  [1]             [2] [1] 

        # a backtracking solution
        # base case

        result = []

        if len(nums) == 1:
            # nums.copy() is slow
            return [nums[:]]

        for i in range(len(nums)):
            # for example we popped 1 from [1,2,3]
            n = nums.pop(0)
            perms = self.permute(nums)

            # add all single elements together 
            # to get the permutation
            for perm in perms:
                perm.append(n)
            # add current permutation to result
            result.extend(perms)
            # add back the number we popped
            # this will change the order in nums, so we
            # traverse in exactly the way we want
            nums.append(n)
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.permute(nums = [1,2,3]))
    print(sol.permute(nums = [0,1]))
    print(sol.permute(nums = [1]))

    print(sol.permute_(nums = [1,2,3]))
    print(sol.permute_(nums = [0,1]))
    print(sol.permute_(nums = [1]))
