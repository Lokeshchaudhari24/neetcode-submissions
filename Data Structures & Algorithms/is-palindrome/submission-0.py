class Solution:
    def isPalindrome(self, s: str) -> bool:
        joined = "".join(ch.lower() for ch in s if ch.isalnum())
        l,r=0,len(joined)-1
        while l<r:
            if joined[l]!=joined[r]:
                return False
            l+=1
            r-=1
        return True
        