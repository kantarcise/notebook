"""
Given an array of integers nums containing n + 1 
integers where each integer is in the range [1, n] 
inclusive.

There is only one repeated number in nums, 
return this repeated number.

You must solve the problem without modifying the 
array nums and uses only constant extra space.
 

Example 1:

    Input: nums = [1,3,4,2,2]
    Output: 2

Example 2:

    Input: nums = [3,1,3,4,2]
    Output: 3

Constraints:

    1 <= n <= 10^5
    nums.length == n + 1
    1 <= nums[i] <= n
    All the integers in nums appear only once except
     for precisely one integer which appears two or more times.

Follow up:

    How can we prove that at least one duplicate 
        number must exist in nums?
 
    Can you solve the problem in linear runtime complexity?

Takeaway:

    You can use a dict but it wont cut it, because it wont be o(1) time

    It is pretty incredible but this is a Linked List question
    [1,3,4,2,2] has length of 5 and the values has to 
    be between 1 - 4

    these are not values, these are pointers

    # i =  0  1  2  3  4 
    # n =  1  3  4  2  2

    If there are a node which is pointed by more than 1 node
    we solve the problem 

    after you find the first intersection of slow and fast pointers
    start a new slow pointer from the beginning, when 
    it meets the old slow pointer, you found your solution

"""

class Solution:
    
    def findDuplicate_(self, nums) -> int:
        # using a dict is not goint to cut it
        # because it will be using o(n) memory

        # DOES NOT MEET REQuirements
        
        # first thing I would try is to use a hashmap
        
        element_freq = {}
        for elem in nums:
            element_freq[elem] = element_freq.get(elem, 0) + 1

        return max(element_freq, key = element_freq.get)


    def findDuplicate(self, nums):
        # It is pretty incredible but this is a Linked List question
        # [1,3,4,2,2] has length of 5 and the values has to 
        # be between 1 - 4

        # these are not values, these are pointers
          
        # i =  0  1  2  3  4 
        # n =  1  3  4  2  2

        # If there are a node which is pointed by more than 1 node
        # we solve the problem 

        # after you find the first intersection of slow and fast pointers
        # start a new slow pointer from the beginning, when 
        # it meets the old slow pointer, you found your solution

        slow, fast = 0, 0
        
        # a do while loop
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow_2 = 0
        while True:
            slow = nums[slow]
            slow_2 = nums[slow_2]
            if slow == slow_2:
                return slow


if __name__ == '__main__':
    sol = Solution()    
    print(sol.findDuplicate(nums = [1,3,4,2,2])) # 2
    print(sol.findDuplicate(nums = [3,1,3,4,2])) # 3
