# Move All Zeroes to End

#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	
    	l=[]
    	l1=[]
    	
        for i in arr:
            if i!=0:
                l.append(i)
            else:
                l1.append(i)
        arr[:]=l+l1
        return arr
    	
