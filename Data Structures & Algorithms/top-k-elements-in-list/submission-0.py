class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        sorted_item=sorted(hashmap.items(),key=lambda x:x[1],reverse=True)
        return [num for num,frequency in sorted_item[:k]]

        