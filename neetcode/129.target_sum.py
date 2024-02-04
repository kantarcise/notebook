"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one 
of the symbols '+' and '-' before each integer in nums and 
then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 
and a '-' before 1 and concatenate them to build the 
expression "+2-1".

Return the number of different expressions that you 
can build, which evaluates to target.
 

Example 1:

Input: nums = [1,1,1,1,1], target = 3

Output: 5

Explanation: There are 5 ways to assign symbols to 
    make the sum of nums be target 3.

            -1 + 1 + 1 + 1 + 1 = 3
            +1 - 1 + 1 + 1 + 1 = 3
            +1 + 1 - 1 + 1 + 1 = 3
            +1 + 1 + 1 - 1 + 1 = 3
            +1 + 1 + 1 + 1 - 1 = 3

        
Example 2:

Input: nums = [1], target = 1

Output: 1


Constraints:

    1 <= nums.length <= 20
    0 <= nums[i] <= 1000
    0 <= sum(nums[i]) <= 1000
    -1000 <= target <= 1000

Takeaway:

The key is to understand the parameters on the decision tree

Which in this case is index and total.

Fantastic Long Summary down below. 

"""

"""
Long Explanaiton:

This post will walk you through the THINKING process behind Dynamic 
Programming so that you can solve these questions on your own.

Category
Most dynamic programming questions can be boiled down to a few categories. 
It's important to recognize the category because it allows us to FRAME a 
new question into something we already know. Frame means use the 
framework, not copy an approach from another problem into the 
current problem. You must understand that every DP problem is different.

Question: Identify this problem as one of the categories below before continuing.

    0/1 Knapsack
    Unbounded Knapsack
    Shortest Path (eg: Unique Paths I/II)
    Fibonacci Sequence (eg: House Thief, Jump Game)
    Longest Common Substring/Subsequeunce

Answer: 0/1 Knapsack

Why 0/1 Knapsack? Our 'Capacity' is the target we want to reach 'S'. 
Our 'Items' are the numbers in the input subset and the 'Weights' of 
the items are the values of the numbers itself. This question follows 
0/1 and not unbounded knapsack because we can use each number ONCE.

What is the variation? The twist on this problem from standard knapsack 
is that we must add ALL items in the subset to our knapsack. We can 
reframe the question into adding the positive or negative value of the 
current number to our knapsack in order to reach the target capacity 'S'.

States
What variables we need to keep track of in order to reach our optimal 
result? 

Here is detailed explaination:

A state is usually defined as the particular condition that 
something is in at a specific point of time.

Similarly, in terms of Dynamic Programming, a state is 
defined by a number of necessary variables at a particular 
instant that are required to calculate the optimal result. 
So, basically it is a combination of variables that will keep 
changing over different instants. More the number of states, 
more is the depth of the recursive solution and more is the 
memory required to cache the result of the states to avoid re-computing. 

This is because, you are most likely to have the same state at some 
point later. Two states are same, if all their corresponding variables 
have the same logical value. Therefore, it very well makes sense to 
preserve the results of the state to save time. This gives rise to 
what is known as Dynamic Programming.

Question: Determine State variables.

Hint: As a general rule, Knapsack problems will require 2 states at minimum.

Answer: Index and Current Sum

Why Index? 

Index represents the index of the input subset we 
are considering. This tells us what values we have considered, 
what values we haven't considered, and what value we are currently 
considering. As a general rule, index is a required state in nearly 
all dynamic programming problems, except for shortest paths which 
is row and column instead of a single index but we'll get into 
that in a seperate post.

Why Current Sum? 

The question asks us if we can sum every item (either the positive 
or negative value of that item) in the subset to reach the target
value. Current Sum gives us the sum of all the values we have 
processed so far. Our answer revolves around Current Sum being 
equal to Target.

Decisions

Dynamic Programming is all about making the optimal decision. 
In order to make the optimal decision, we will have to try all 
decisions first. The MIT lecture on DP (highly recommended) refers 
to this as the guessing step. My brain works better calling this a 
decision instead of a guess. Decisions will have to bring us closer 
to the base case and lead us towards the question we want to answer. 
Base case is covered in Step 4 but really work in tandem with the 
decision step.

Question: What decisions do we have to make at each recursive call?

Hint: As a general rule, Knapsack problems will require 2 decisions.

Answer: This problem requires we take ALL items in our input subset, 
so at every step we will be adding an item to our knapsack. Remember, 
we stated in Step 2 that "The question asks us if we can sum every 
item (either the positive or negative value of that item) in the 
subset to reach the target value." The decision is:

Should we add the current numbers positive value
Should we add the current numbers negative value

As a note, knapsack problems usually don't require us to take all 
items, thus a usual knapsack decision is to take the item or leave the item.

Base Case

Base cases need to relate directly to the conditions required by 
the answer we are seeking. This is why it is important for our 
decisions to work towards our base cases, as it means our decisions 
are working towards our answer.

Let's revisit the conditions for our answers.

We use all numbers in our input subset.
The sum of all numbers is equal to our target 'S'.
Question: Identify the base cases.
Hint: There are 2 base cases.

Answer: We need 2 base cases. One for when the current state is valid 
and one for when the current state is invalid.

Valid: Index is out of bounds AND current sum is equal to target 'S'
Invalid: Index is out of bounds
Why Index is out of bounds? A condition for our answer is that we use 
EVERY item in our input subset. When the index is out of bounds, we know 
we have considered every item in our input subset.

Why current sum is equal to target? A condition for our answer is that 
the sum of using either the positive or negative values of items in our 
input subet equal to the target sum 'S'.

If we have considered all the items in our input subset and our current 
sum is equal to our target, we have successfully met both conditions 
required by our answer.

On the other hand, if we have considered all the items in our input subset 
and our current sum is NOT equal to our target, we have only met condition 
required by our answer. No bueno.

Code it

If you've thought through all the steps and understand the problem, it's 
trivial to code the actual solution.

 def findTargetSumWays(self, nums, S):
     index = len(nums) - 1
     curr_sum = 0
     return self.dp(nums, S, index, curr_sum)
     
 def dp(self, nums, target, index, curr_sum):
 	# Base Cases
     if index < 0 and curr_sum == target:
         return 1
     if index < 0:
         return 0 
     
 	# Decisions
     positive = self.dp(nums, target, index-1, curr_sum + nums[index])
     negative = self.dp(nums, target, index-1, curr_sum + -nums[index])
     
     return positive + negative
Optimize
Once we introduce memoization, we will only solve each subproblem ONCE. We can 
remove recursion altogether and avoid the overhead and potential of a stack 
overflow by introducing tabulation. It's important to note that the top down 
recursive and bottom up tabulation methods perform the EXACT same amount of 
work. The only different is memory. If they peform the exact same amount of 
work, the conversion just requires us to specify the order in which problems 
should be solved. This post is really long now so I won't cover these steps 
here, possibly in a future post.

Memoization Solution for Reference

class Solution:
    def findTargetSumWays(self, nums, S):
        index = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.dp(nums, S, index, curr_sum)
        
    def dp(self, nums, target, index, curr_sum):
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]
        
        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0 
        
        positive = self.dp(nums, target, index-1, curr_sum + nums[index])
        negative = self.dp(nums, target, index-1, curr_sum + -nums[index])
        
        self.memo[(index, curr_sum)] = positive + negative
        return self.memo[(index, curr_sum)]

DP IS EASY!

Thanks.

"""

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        # neet
        
        # brute force is a decision tree
        
        # we either add or subtract the number
        
        # we can use (index and total)
        # index is for to see where should we stop
        # target is for to find the result
        
        #             (0, 0)
        #          +1 /      \ -1
        #        (1, 1)       (1, -1) 
        #     +1 /     \ -1 
        #   (2, 2)      (2, 0)
        
        # and goes on..
        
        # if we start at index , and total
        # how many ways can we get to the target?
        dp = {}  # (index, total) -> # of ways
        
        def backtrack(i, total):
            if i == len(nums):
                # reached at the end of the array
                return 1 if total == target else 0
            
            # if this value is calculated before
            if (i, total) in dp:
                return dp[(i, total)]
            
            # we either add the current indexed number to total
            # or we subtract it!
            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) +
                             backtrack(i + 1, total - nums[i]))
            
            return dp[(i, total)]
        
        # start from index 0, 
        # total at the start is also 0
        return backtrack(0, 0)
