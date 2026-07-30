class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixs=[1]
        sufixs=[1]*len(nums)
        ans=[]
        for i in range(1,len(nums)):
            prefixs.append(prefixs[i-1]*nums[i-1])
        for i in range(len(nums)-2,-1,-1):
            sufixs[i]=sufixs[i+1]*nums[i+1]
        for i in range(len(nums)):
            ans.append(sufixs[i]*prefixs[i])
        return ans
        