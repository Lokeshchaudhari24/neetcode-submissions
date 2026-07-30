class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort=set(nums)
        length=0
        maxl=0
        for i in sort:
            if i-1 not in  sort:
                length=1
                cur=i
                maxl=max(maxl,length)
                while cur+1 in sort:
                    length+=1
                    maxl=max(maxl,length)
                    cur+=1
        return maxl

                    
