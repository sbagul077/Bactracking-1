class Solution:
    def helper(self, candidates, target, result, path):
        # base
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(0, len(candidates)):
            newLi = list(path)
            newLi.append(candidates[i])
            self.helper(candidates[i:], target - candidates[i], result, newLi)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.helper(candidates, target, result, [])
        return result
