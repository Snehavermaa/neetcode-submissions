class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        
        if l1>l2:
            return False
        count1=[0]*26
        count2=[0]*26
        
        for i in range(l1):
            count1[ord(s1[i])-ord('a')]+=1
        
        l=0

        for r in range(l2):
            count2[ord(s2[r]) - ord('a')]+=1
            if r-l+1> l1:
                count2[ord(s2[l]) - ord('a')]-=1
                l+=1
            if count1==count2:
                return True
        return False
