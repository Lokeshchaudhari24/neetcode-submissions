class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        
        # Frequency arrays for 26 lowercase English letters
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        for i in range(len1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        # Sliding window
        left = 0
        for right in range(len1, len2):
            if s1_count == s2_count:
                return True
            
            # Add new character to the window
            s2_count[ord(s2[right]) - ord('a')] += 1
            # Remove old character from the left of the window
            s2_count[ord(s2[left]) - ord('a')] -= 1
            left += 1
            
        # Check the last window
        return s1_count == s2_count
        