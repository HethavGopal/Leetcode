class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res, curSet = [], []

        def dfs(i,curSet,total):

            # Base cases
            if total > target:
                return         
    
            if total == target:
                res.append(curSet.copy())
                return
            
            if i >= len(candidates):
                return
            
            # Incl case
            curSet.append(candidates[i])            
            dfs(i, curSet, total + candidates[i])
            curSet.pop()

            #skip case
            dfs(i + 1, curSet, total)
            
        dfs(0,[],0)
        return res

            



        
        



        
        
        