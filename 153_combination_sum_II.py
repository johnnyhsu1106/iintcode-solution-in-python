'''
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

 Notice

All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.

Example
Given candidate set [10,1,6,7,2,1,5] and target 8,

A solution set is:

[
  [1,7],
  [1,2,5],
  [2,6],
  [1,1,6]
]
'''
class Solution:
    """
    @param: num: Given the candidate numbers
    @param: target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target):
        '''
        Please see the problem 018 and 135
        '''

        if not candidates:
            return []

        candidates.sort()

        start_index = 0
        combination = []
        remains = target
        results = []

        self._dfs(candidates, start_index, combination, remains, results)

        return results


    def _dfs(self, candidates, start_index, combination, remains, results):
        #  base case (stoppig condition)
        if remains == 0:
            results.append(combination.copy())
            return

        for i in range(start_index, len(candidates)):
            if candidates[i] > remains:
                break

            if i == 0 or candidates[i] != candidates[i - 1] or i == start_index:
                combination.append(candidates[i])
                self.dfs(candidates, i + 1, combination, remains - candidates[i], results)
                combination.pop()

# def main():
#     s = Solution()
#     candidate = [10,1,6,7,2,1,5]
#     target = 8
#     print(s.combinationSum2(candidate, target))
#     # A solution set is:
#     #
#     # [
#     #   [1,7],
#     #   [1,2,5],
#     #   [2,6],
#     #   [1,1,6]
#     # ]
# if __name__ == '__main__':
#     main()
