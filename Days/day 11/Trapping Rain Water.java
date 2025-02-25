class Solution {
    public int maxWater(int arr[]) {
        // code here
        int n=arr.length;
        int [] left = new int[n];
        int [] right = new int[n];
        
        int res=0;
        left[0]=arr[0];
        for(int i=1;i<n;i++){
            
            left[i]=Math.max(left[i-1],arr[i]);
            
        }
        right[n-1]=arr[n-1];
        for(int i=n-2;i>=0;i--){
            
            right[i]=Math.max(right[i+1],arr[i]);
        }
        
        //calculate accumulate water element
        
        for(int i=1;i<n-1;i++){
            
            int minof2=Math.min(left[i-1],right[i+1]);
            
            if(minof2>arr[i]){
                res+=minof2-arr[i];
            }
        }
        return res;
    }
}
