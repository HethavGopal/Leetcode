class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        curSet, res = [], []
        total = 0
        
        

        def dfs(i, total):
        
        
            if total == target:
                res.append(curSet.copy())
                return
            elif total > target:
                return 
            
            if i >= len(candidates):
                return
            
            
            # Include current index
            curSet.append(candidates[i])
            dfs(i, total + candidates[i])
            curSet.pop()
            
            # Skip index
            dfs(i + 1, total)

        
        dfs(0,total)

        return res


















