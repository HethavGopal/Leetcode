class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        curSet, res = [], []

        def dfs():
            if len(curSet) == len(nums):
                res.append(curSet.copy())

            for num in nums:
                if num in curSet:
                    continue 

                curSet.append(num)
                dfs()
                curSet.pop()

        dfs()     
        return res   


            

           



