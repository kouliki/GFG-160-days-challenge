class Solution {
    public static boolean check(int []arr, int k, int pagelimit){
        
        int c=1;
        int pagesum=0;
        
        for(int i=0;i<arr.length;i++){
            
            if(pagesum+arr[i]>pagelimit){
                
                c++;
                pagesum=arr[i];
            }
            else{
                pagesum+=arr[i];
            }
        }
        return (c<=k);
    }
    
    
    public static int findPages(int[] arr, int k) {
        // code here
        if(k>arr.length){
            return -1;
            
        }
        int l=Arrays.stream(arr).max().getAsInt();
        int h=Arrays.stream(arr).sum();
        int res=-1;
        while(l<=h){
            int mid=l+(h-l)/2;
            if(check(arr,k,mid)){
                res=mid;
                h=mid-1;
            }
            else{
                l=mid+1;
            }
        }
        return res;
    }
}
