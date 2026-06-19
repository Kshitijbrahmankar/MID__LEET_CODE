class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort() 

        def backtracking(start, remaining , path):
            if remaining == 0:
                result.append(path[:])
                return 
            
            if remaining < 0:
                return 
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtracking(i+1, remaining-candidates[i],path)
                path.pop()

        backtracking(0,target,[])
        return result