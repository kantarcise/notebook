"""

Given an array of integers temperatures represents the daily 
temperatures, return an array answer such that answer[i] is the number of 
days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which 
this is possible, keep answer[i] == 0 instead.

 
Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100


Takeaway:

To hold the previous values while traversing a list, a list or a stack can be useful.

Initialize the result list, as it is simply the same size as the given sequence.

while control flow is wonderful with more than one booleans. Try to 
perfect the iteration with multiple conditions

"""

class Solution:

    """
    Your current approach is straightforward and works by comparing each day's temperature 
    with the temperatures of all future days to find the first warmer day. However, this
     approach has a time complexity of O(n^2) because for each day, you iterate through
      the remaining days to find a warmer day. Given the constraints
       (1 <= temperatures.length <= 105), this approach is not efficient and will likely
    time out for large input arrays.

    To improve the time complexity, you can use a stack-based approach. The idea
     is to maintain a stack of indices of the temperatures that you haven't found a
      warmer day for yet. When you encounter a higher temperature, you can quickly
    determine how many days you have to wait for a warmer temperature for the
    indices stored in the stack.

    Here's an outline of the improved algorithm:

    1) Initialize an empty stack to store indices.

    2) Initialize an array result of the same length as temperatures to store the waiting
     days. Initialize all values in result to 0.

    3) Iterate through temperatures from left to right.

    4) For each temperature, check if the stack is not empty, and if the current temperature
    is higher than the temperature at the index stored at the top of the stack. If it
    is, pop the index from the stack and calculate the waiting days as the current
    day minus the popped index. Set the corresponding value in result to the 
    waiting days.

    5) Push the current index onto the stack.

    6) Continue this process for all temperatures.

    7) Return the result array, which contains the waiting days.

    This stack-based approach has a time complexity of O(n) because each day's 
    temperature is pushed onto and popped from the stack at most once. It is a 
    more efficient solution for this problem.
    """
    # first try
    def dailyTemperatures_(self, temperatures):
        # we are measuring the time difference between days where temp_latter > temp_now
        # [73,74,75,71,69,72,76,73]
        # for first day, next day higher so 1
        # for second day, next day higher so 1
        # for second day, next day higher so 1
        # for third day, next high is 4 days later

        # we have to make the comparison between current day and days withing the list.

        result = []

        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result.append(j - i)
            result.append(0)

        return result

    def dailyTemperatures_brute_force(self, temperatures):
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break
        return ans

    def dailyTemperatures(self, temperatures):
        # initialize a stack we will store indices here.
        #  previous days' indices
        # it is a monotonic decreasing stack.
        stack = []
        # we will hold the results in a list
        result = [0] * len(temperatures)

        # traverse the temperature lists
        for index, element in enumerate(temperatures):
            # check whether current val is greater than the last appended stack value. 
            #  We will pop all the elements which is lesser than the current temp

            while stack and temperatures[stack[-1]] < element:
                j = stack.pop()
                result[j] = index - j
            # after you are done calculating the result, add 
            # the index to the stack
            stack.append(index)

        return result

    
    def dailyTemperatures_elem_index_pair(self, temperatures):
        res = [0] * len(temperatures)
        stack = []  # pair, [temperature, index]

        for index, elem in enumerate(temperatures):
            while stack and elem > stack[-1][0]:
                stack_temp , stack_index = stack.pop()
                res[stack_index] = (index - stack_index)
            stack.append([elem, index])

        return res



if __name__ == "__main__":
    
    sol = Solution()
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
    print(sol.dailyTemperatures([30,40,50,60]))
    print(sol.dailyTemperatures([30,60,90]))
