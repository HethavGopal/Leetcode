class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0

        L,R = 0, 0

        for R in range(len(s)):
            if s[R] not in seen:
                seen.add(s[R])
                max_len = max(len(seen),max_len)
                continue 
            else:
                while s[R] in seen:
                    seen.remove(s[L])
                    L += 1
                seen.add(s[R])
        
        return max_len

        




            

            



        