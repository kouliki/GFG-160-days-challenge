# Second Largest

class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        if len(arr)<2:
            return -1
        a=list(set(arr))
        if len(a)<2:
            return -1
        
        
        a.sort()
        return a[-2]


