class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        curSet, res = [],[]
        
        def dfs(i , curSet):
            if i >= len(nums):
                res.append(curSet.copy())
                return
            
            # incl num
            curSet.append(nums[i])
            dfs(i + 1, curSet)
            curSet.pop()

            #skip num
            dfs(i + 1, curSet)
        
        dfs(0,[])
        return res

            

        
        