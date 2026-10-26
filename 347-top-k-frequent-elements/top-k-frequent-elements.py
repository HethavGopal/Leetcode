class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket_sort = [[] for _ in range(len(nums))]
        res = []

        # Count nums
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 0

        # put into bucket sort
        for num in count:
            freq = count[num]
            bucket_sort[freq].append(num)
        
        # return k freq element

        i = len(bucket_sort) - 1
        while len(res) < k:
            if bucket_sort[i]:
                for n in range(len(bucket_sort[i])):
                    res.append(bucket_sort[i][n])
            i -= 1

        return res

            





            

                
    

