"""
Given an integer array nums, return an array answer such that answer[i] is equal
 to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without
 using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]


Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output
 array does not count as extra space for space complexity analysis.)

Takeaway:

If you multiply every element to the left and to the right, 
you will get the product of all elements.


"""

class Solution:

    def first_product_except_self(self, seq):
        
        answer = []
        # product of all elements except the index loop is iterating
        for index in range(len(seq)):
            # multiply every element of nums
            temp_list = list(seq)
            temp_list.remove(temp_list[index])
            _product = 1
            # this is now o(n^2) - NOT GOOD 
            for elem in temp_list:
                _product *= elem 
            answer.append(_product)
        return answer

    def productExceptSelf(self, nums):
        """This method basically uses the idea of product of
         all elements to the left and right for every
          element and when we multiplty the results, we
         get product of all elements except index'th element"""
        
        n = len(nums)
        result = [1] * n
        
        # Compute products to the left of each element 
        # and store in the result array
        left_product = 1
        for i in range(n):
            result[i] *= left_product
            left_product *= nums[i]
        
        # Compute products to the right of each element 
        # and update the result array
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result

if __name__ == '__main__':
    
    prod = Solution()

    print("This is my first approach")

    print(prod.first_product_except_self([1,2,3,4]))
    print(prod.first_product_except_self([-1,1,0,-3,3]))

    print("Better approach")

    print(prod.productExceptSelf([1,2,3,4]))
    print(prod.productExceptSelf([-1,1,0,-3,3]))