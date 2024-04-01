"""
Given an array of integers temperatures represents 
the daily temperatures, return an array answer such 
that answer[i] is the number of days you have to wait 
after the ith day to get a warmer temperature. 

If there is no future day for which this is possible,
keep answer[i] == 0 instead.

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

    1 <= temperatures.length <= 10^5
    30 <= temperatures[i] <= 100

Takeaway:

    To hold the previous values while traversing a 
        list, a list or a stack can be useful.

    Initialize the result list, as it is simply the 
        same size as the given sequence.

    While control flow is wonderful with more than 
    one booleans. 
    Try to perfect the iteration with multiple conditions.
"""

class Solution:
    def dailyTemperatures(self, temperatures):
        # we can brute force it
        # it will give the error, time limit exceeded.

        ans = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                # for every element, compare until 
                # find bigger
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break
        return ans

    def dailyTemperatures_(self, temperatures):
        
        # Time complexity of O(n) because each day's 
        # temperature is pushed onto and popped from the stack
        # at most once. It is more efficient.
        
        # stack for storing indices.
        # it is a monotonic decreasing stack.
        stack = []
        
        # we will hold the results in a list
        result = [0] * len(temperatures)

        # traverse the temperature lists
        for index, element in enumerate(temperatures):
            # check whether current val is greater than 
            # the last appended stack value. 
            
            #  We will pop all the elements which is 
            # lesser than the current temp

            while stack and temperatures[stack[-1]] < element:
                # stack is not empty
                # and current value is bigger than top of stack
                j = stack.pop()
                result[j] = index - j
            
            # after you are done calculating the result, add 
            # the index to the stack
            stack.append(index)

        return result
    
    def dailyTemperatures__(self, temperatures):
        # we can hold both temperatures and indexes in the stack
        stack = []  # pair, [temperature, index]

        res = [0] * len(temperatures)

        for index, elem in enumerate(temperatures):
            while stack and elem > stack[-1][0]:
                # element is bigger, update the stack
                # pop old max
                stack_temp , stack_index = stack.pop()
                # calculate result
                res[stack_index] = (index - stack_index)
            # append new elem
            stack.append([elem, index])

        return res

if __name__ == "__main__":
    
    sol = Solution()
    # [1,1,4,2,1,1,0,0]
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
    # [1, 1, 1, 0]
    print(sol.dailyTemperatures([30,40,50,60]))
    # [1, 1, 0]
    print(sol.dailyTemperatures([30,60,90]))

    print(sol.dailyTemperatures_([73,74,75,71,69,72,76,73]))
    print(sol.dailyTemperatures_([30,40,50,60]))
    print(sol.dailyTemperatures_([30,60,90]))

    print(sol.dailyTemperatures__([73,74,75,71,69,72,76,73]))
    print(sol.dailyTemperatures__([30,40,50,60]))
    print(sol.dailyTemperatures__([30,60,90]))
