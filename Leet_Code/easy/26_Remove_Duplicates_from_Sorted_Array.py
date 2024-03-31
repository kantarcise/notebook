"""
Given an integer array nums sorted in non-decreasing order, remove the 
duplicates in-place such that each unique element appears only once. 

The relative order of the elements should be kept the same. 

Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get 
accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums 
        contain the unique elements in the order they were present 
        in nums initially. The remaining elements of nums are not 
        important as well as the size of nums.
    
    Return k.
    
Custom Judge:

The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length

    int k = removeDuplicates(nums); // Calls your implementation

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }
    If all assertions pass, then your solution will be accepted.

Example 1:

    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first 
        two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the 
        returned k (hence they are underscores).

Example 2:

    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first 
        five elements of nums being 0, 1, 2, 3, and 4 respectively.
    It does not matter what you leave beyond the returned 
        k (hence they are underscores).
 
Constraints:

    1 <= nums.length <= 3 * 10^4
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.

Takeaway:

  A set will work. 
  
  You can use the ordered property for your advantage.

"""
class Solution:
    def removeDuplicates_(self, nums: List[int]) -> int:
        # make a set
        # base condition on set
        # return length of set
        s = set()
        s.add(nums[0])
        index = 1
        
        for i in range(len(nums)):
            if nums[i] in s:
                continue
            else:
                # encountered a unique element 
                # starting from index 1, populate the array
                s.add(nums[i])
                nums[index] = nums[i]
                index += 1
                
        return len(s)
    
    def removeDuplicates(self, nums: List[int]) -> int:
        # we do not even need the set
        # because the list is in non-decreasing order
        
        current_unique_index = 0
        
        # keep only last element
        last = None
        
        for n in nums:
            if n == last:
                # if n is the same as the last seen element 
                continue
                
            # a new element encountered
            # update last
            last = n
            # make that index, that element 
            nums[current_unique_index] = n
            # increase index for uniques
            current_unique_index += 1
        
        return current_unique_index

sol = Solution()
print(sol.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))
