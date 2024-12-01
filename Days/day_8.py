# Kadane's Algorithm

#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        
        res=arr[0]
        max_array=arr[0]
        
        for i in range(1,len(arr)):
            max_array=max((max_array+arr[i]),arr[i])
            
            res=max(max_array,res)
        return res
        
