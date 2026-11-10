class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = []
        product = 1

        for num in nums:
            prefix.append(product)
            product *= num
        
        suffix = []
        product = 1

        for num in reversed(nums):
            suffix.append(product)
            product *= num
        
        suffix.reverse()

        res = []
        for i in range(len(nums)):
            ans = suffix[i] * prefix[i]
            res.append(ans)
        
        return res

            





        