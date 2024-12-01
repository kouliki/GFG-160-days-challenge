# Majority Element II

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        
        if len(arr)<1:
            return []
            
        total_votes=len(arr)
        threshold=total_votes//3
      
        d={}
        
        for i in arr:
            if i in d:
                d[i]+=1
                
            else:
                d[i]=1
                
        l=[]
        for candidate,votes in d.items():
            if votes>threshold:
                l.append(candidate)
        
        return sorted(l)
