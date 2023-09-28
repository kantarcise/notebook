"""

There are n cars going to the same destination along a one-lane road. The 
destination is target miles away.

You are given two integer array position and speed, both of length n, where
 position[i] is the position of the ith car and speed[i] is the speed of the
  ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and 
drive bumper to bumper at the same speed. The faster car will slow down to
 match the slower car's speed. The distance between these two cars is 
 ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position
 and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will 
still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

 
Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

Output: 3

Explanation:

The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.

The car starting at 0 does not catch up to any other car, so it is a fleet by itself.

The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other 
at 6. The fleet moves at speed 1 until it reaches target.

Note that no other cars meet these fleets before the destination, so the answer is 3.


Example 2:

Input: target = 10, position = [3], speed = [3]

Output: 1

Explanation: There is only one car, hence there is only one fleet.


Example 3:

Input: target = 100, position = [0,2,4], speed = [4,2,1]

Output: 1

Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting
 each other at 4. The fleet moves at speed 2.

Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one 
fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
 

Constraints:

n == position.length == speed.length
1 <= n <= 105
0 < target <= 106
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 106

Takeaway:

Car that is closest to the target is the bottleneck, becuase of this
reason, we traverse the sequence in reverse.

we can use zip() to combine multiple lists as pairs = [positions, speed]

We can use a stack to compare car duos

Basically using the time that a car going to be at target with its 
speed and whether or not the car behind it will catch up with it

"""


class Solution:

    # first try
    def carFleet(self, target, position, speed):
        # for each car, critical bottleneck is their starting position
        # we can simulate the environment with each speed added to 
        # the positions every unit time

        fleet_count = 0        
        # if a car reaches target, it can leave 
        current_position = position.copy()

        while min(current_position) < target:
            current_position = [a + b for a, b in zip(current_position, speed)]
            for index, elem in enumerate(current_position):
                if elem > target:
                    fleet_count += 1
                # remove that element
        return fleet_count

    def car_fleet_stack(self, target, position, speed):
        
        # make the pairs
        pair = [[p, s] for p, s in zip(position, speed)]
        
        # how many care fleets we have
        stack = []

        # traverse in reverse order because the car that is closest 
        # to target is the bottleneck
        for p, s in sorted(pair, reverse = True): # reverse sorted order
            stack.append((target - p) / s)
            # we need at least 2 elements to compares
            # compare the times for two elements
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # there is a collision
                stack.pop()
        return len(stack)


    def car_fleet_multiple_lists(self, target, position, speed):
        # the time will be collected to 'time' array, 
		# but first let's put the dist and speed to keep track of correct speed for dist
		# after we sort
        time = []
        
        for i in range(len(position)):
            time.append((position[i], speed[i]))
        time.sort(key=lambda x: x[0])
    
        # let's calculate the time keeping the decimal points in place
        for idx, distSpeed in enumerate(time):
            time[idx] = float(target - distSpeed[0]) / distSpeed[1]
        
        # We know that if the car behind takes more time to reach the target
        # then, that means the two car is separated, so we will increase the fleet count
        fleetCount = 0
        
        # fleetLeaderTime represent, whenever we find new fleet,
        # we want every car in the fleet to take less time than the
        # head(lead) of the fleet's time taken
        fleetLeaderTime = 0
        
        for i in range(len(time) - 1, -1, -1):
            curr = time[i]
            # if currCar's time need to achieve the target is less than
            # the head of fleet, then the car is part of the fleet
            # otherwise, we found separate fleet, so increment, and update the
            # 'fleetLeaderTime'
            if curr > fleetLeaderTime:
                fleetCount += 1
                fleetLeaderTime = curr
        
        return fleetCount

if __name__ == "__main__":
    sol = Solution()
    print(sol.car_fleet_stack(12, [10,8,0,5,3], [2,4,1,1,3]))
    print(sol.car_fleet_stack(10, [3], [3]))
    print(sol.car_fleet_stack(100, [0,2,4], [4,2,1]))

    print(sol.car_fleet_multiple_lists(12, [10,8,0,5,3], [2,4,1,1,3]))
    print(sol.car_fleet_multiple_lists(10, [3], [3]))
    print(sol.car_fleet_multiple_lists(100, [0,2,4], [4,2,1]))
