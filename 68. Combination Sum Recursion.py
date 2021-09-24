class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def helper(candidates, target, path):
            if target == 0:
                result.append(path)
                return

            if target < 0 or index == len(candidates):
                return

            for i in range(len(candidates)):
                helper(candidates[i:], target - candidates[i], path + [candidates[i]])

        helper(candidates, target, [])
        return result