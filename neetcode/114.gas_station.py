"""
There are n gas stations along a circular route, where the amount 
of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of 
gas to travel from the ith station to its next (i + 1)th station. 
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas 
station's index if you can travel around the circuit once in 
the clockwise direction, otherwise return -1. If there exists 
a solution, it is guaranteed to be unique.

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
 
Constraints:

n == gas.length == cost.length
1 <= n <= 105
0 <= gas[i], cost[i] <= 104


Takeaway:

Understanding the question is key.

Greedy approach is just understanding the simple example given.

Total sums and movement at every step is key.

"""
class Solution:
    def canCompleteCircuit_(self, gas: list[int], cost: list[int]) -> int:
        """This did NOT work."""
        # gas[i], all stations
        # cost[i] - cost to travel the next station - not money, gas consumption
        # where should we start to complete a lap in clockwise direction?
        
        # brute force
        # try every start and see if you can 
        # keep gas higher or equal to 0
        
        def reach(i, gas_list, cost_list):
            total = zip(gas_list, cost_list)
            
            sub_sum = 0
            for i in range(0, len(gas_list)):
                sub_sum += total[0] - total[1]
            
            return True if sub_sum >= 0 else False
        
        # total = 0
        # for gas, cost in zip(gas,cost):
        #     total += (gas - cost)
        # return total if total >= 0 else -1        
        
        for i in range(len(gas)):
            if reach(i, gas, cost):
                return i
            else:
                pass
      
        return -1
        
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # we can easily see that sum of total gas should 
        # be greater or equal to sum of cost 
        
        # gas        =  [1, 2, 3, 4, 5]
        # cost       =  [3, 4, 5, 1, 2]
        # difference =  [-2,-2,-2,3, 3]
        
        # starting from the beginning 
        # we will try out positions
        # if difference is (-) we cannot select that position
        # go to the next and start again
        
        # does a solution exist ?
        if sum(gas) < sum(cost):
            return -1
        
        # if there is indeed a solution
        total = 0
        result_position = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            
            # if total dips below zero, this position will not work
            if total < 0:
                total = 0
                result_position = i + 1
                
        return result_position