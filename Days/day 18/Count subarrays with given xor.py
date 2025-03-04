class Solution:
    def subarrayXor(self, arr, k):
        # code here
        
        xor_map={}
        c=0
        prefix_xor=0
        
        for i in arr:
            prefix_xor^=i
            
            if prefix_xor==k:
                c+=1
            target_xor=prefix_xor^k
            if target_xor in xor_map:
                c+=xor_map[target_xor]
            xor_map[prefix_xor]=xor_map.get(prefix_xor,0)+1
        
        return c
