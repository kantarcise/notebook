"""
You start with an initial power of power, an initial 
score of 0, and a bag of tokens given as an integer 
array tokens, where each tokens[i] donates the 
value of tokeni.

Your goal is to maximize the total score by strategically 
playing these tokens. In one move, you can play an 
unplayed token in one of the two ways (but not both 
for the same token):

Face-up: If your current power is at least tokens[i], 
  you may play tokeni, losing tokens[i] power and 
  gaining 1 score.

Face-down: If your current score is at least 1, you 
  may play tokeni, gaining tokens[i] power and losing 
  1 score.

Return the maximum possible score you can achieve 
after playing any number of tokens.

Example 1:

Input: tokens = [100], power = 50

Output: 0

Explanation: Since your score is 0 initially, you 
cannot play the token face-down. You also cannot play 
it face-up since your power (50) is less 
than tokens[0] (100).

Example 2:

Input: tokens = [200,100], power = 150

Output: 1

Explanation: Play token1 (100) face-up, reducing your 
power to 50 and increasing your score to 1.

There is no need to play token0, since you cannot play 
it face-up to add to your score. The maximum score 
achievable is 1.

Example 3:

Input: tokens = [100,200,300,400], power = 200

Output: 2

Explanation: Play the tokens in this order to get a score of 2:

Play token0 (100) face-up, reducing power to 100 and increasing score to 1.
Play token3 (400) face-down, increasing power to 500 and reducing score to 0.
Play token1 (200) face-up, reducing power to 300 and increasing score to 1.
Play token2 (300) face-up, reducing power to 0 and increasing score to 2.
The maximum score achievable is 2.

Constraints:

0 <= tokens.length <= 1000
0 <= tokens[i], power < 104

Takeaway:

  Setting the conditions right is everything here. Use the examples.

"""

from collections import deque
from itertools import islice

# islice('ABCDEFG', 2) --> A B
# islice('ABCDEFG', 2, 4) --> C D
# islice('ABCDEFG', 2, None) --> C D E F G
# islice('ABCDEFG', 0, None, 2) --> A C E G

class Solution:
    def bagOfTokensScore_(self, tokens: list[int], power: int) -> int:
        # my approach did not work
        # islice only works with positive integers
        # we can sort tokens

        # we want to gain scores with lowest tokes possible
        # we should lose scores with biggest tokens possible
        tokens.sort()
        tok = deque(tokens)
        score = 0
        while tok[0] < power:
            power -= tok[0]
            score += 1
            tok.popleft()

        # remaining elements balance
        # try all combinations
        for i in range(len(tok)):
            print(i)
            if sum(islice(tok, -1, i-2, -1 )) + power > sum(tok[:-1]):
                score += len(tok[:-1])
        
        return score
    
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        tokens = deque(tokens)
        score = 0
        max_score = 0

        # until we still have a logical move
        while tokens and (power >= tokens[0] or score > 0):
            while tokens and power >= tokens[0]:
                # face up play
                power -= tokens.popleft()
                score += 1
                
            # max possible score
            max_score = max(max_score, score)

            if tokens and score > 0:
                # face down play
                power += tokens.pop()
                score -= 1
                # we will try again with new power

        return max_score
