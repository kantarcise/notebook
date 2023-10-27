"""
Given an integer array nums and an integer k, 
return the kth largest element in the array.

Note that it is the kth largest element in the 
sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:

    1 <= k <= nums.length <= 105
    -104 <= nums[i] <= 104

Takeaway:

instead of sorting - o(nlogn)
we can use a heap

every time we pop an element from the heap
it is log n
so this result will be - o(n + k log n)

There is a solution whick uses quick_select
which is kinda like quick_sort

"""
from heapq import heapify, heappop

class Solution:

    def find_kth_largest(self, nums: "list[int]", k: int) -> int:
        # instead of sorting - o(nlogn)
        # we can use a heap

        # every time we pop an element from the heap
        # it is log n
        # so this result will be - o(n + k log n)

        negative = [-elem for elem in nums]
        heapify(negative)
        # now we have a max heap
        # for [3,2,1,5,6,4] - negative - [-6, -5, -4, -3, -2, -1]
        
        for _ in range(k):
            result = heappop(negative)
            
        return -result

    def find_kth_largest(self, nums: "list[int]", k: int) -> int:
        # with sorting
        nums.sort(reverse = True)
        return nums[k - 1]

    def findKthLargest(self, nums: "list[int]", k: int) -> int:
        # neet code 
        # quick select - kinda like quicksort
        # average case o(n) - worst case o(n**2)
        
        # if the array is sorted
        # kth largest element is:
        k  = len(nums) - k

        # left and right pointers
        def quick_select(l, r):
            # let pivot bve the rightmost element
            # p is just left pointer
            pivot, p = nums[r], l
            # iterate over the list, except last element
            for i in range(l, r):
                # 
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    # onto next position
                    p += 1
            # swapping the rightmost element with current 
            # position of the pointer
            nums[p], nums[r] = nums[r], nums[p]


            if p > k :
                # look at the left portion
                return quick_select(l , p - 1)
            elif p < k:
                # look at the right portion
                return quick_select(p + 1, r)
            else: 
                # we found the element
                return nums[p]

        return quick_select(0, len(nums) - 1)