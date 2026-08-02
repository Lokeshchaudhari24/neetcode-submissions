class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        maxc=0
        while r<len(s):
            if s[r] not in s[l:r]:
                maxc=max(maxc,r-l+1)
            else:
                while s[r] in s[l:r]:
                 l+=1

            r+=1
        return maxc


        