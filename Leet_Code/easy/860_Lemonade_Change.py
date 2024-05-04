"""
At a lemonade stand, each lemonade costs $5. 

Customers are standing in a queue to buy from you 
and order one at a time (in the order specified by bills). 

Each customer will only buy one lemonade and pay
with either a $5, $10, or $20 bill. 

You must provide the correct change to each 
customer so that the net transaction is that 
the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill 
the ith customer pays, return true if you can provide
every customer with the correct change, or 
false otherwise.

Example 1:

    Input: bills = [5,5,5,10,20]
    
    Output: true
    
    Explanation: 
        
        From the first 3 customers, we collect three $5 bills in order.
        From the fourth customer, we collect a $10 bill and give back a $5.
        From the fifth customer, we give a $10 bill and a $5 bill.
        Since all customers got correct change, we output true.

Example 2:

    Input: bills = [5,5,10,10,20]
    
    Output: false
    
    Explanation: 
        From the first two customers in order, we collect two $5 bills.
        For the next two customers in order, we collect 
            a $10 bill and give back a $5 bill.
        For the last customer, we can not give the change 
            of $15 back because we only have two $10 bills.
        Since not every customer received the correct 
            change, the answer is false.
 
Constraints:

    1 <= bills.length <= 105
    
    bills[i] is either 5, 10, or 20.

Takeaway:

    Always question, best conceiveable runtime.

"""

class Solution:
    def lemonadeChange_(self, bills: List[int]) -> bool:
        pocket = {5 : 0, 10 : 0, 20: 0}
        
        for elem in bills:
            if elem == 5:
                pocket[5] += 1
            elif elem == 10:
                pocket[10] += 1
                pocket[5] -= 1
                if pocket[5] < 0:
                    return False
            else:
                pocket[20] += 1
                # 2 possible approaches
                if pocket[10] >= 1 and pocket[5] >= 1:
                    pocket[5] -= 1
                    pocket[10] -= 1
                    
                elif pocket[5] >= 3:
                    pocket[5] -= 3
                else:
                    return False
        
        return True
    
    def lemonadeChange(self, bills: List[int]) -> bool:
        # can we get to a better solution ?
        # yes!
        # this one is 
        # O(n) time a O(1) space
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
