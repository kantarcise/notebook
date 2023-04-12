# Needs work and thinking.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows + 1):
            row = [1] * i
            for j in range(1,i-1):
                row[j] = ans[i - 2][j] + ans[i - 2][j - 1]
            ans.append(row)
        return ans
