
class Solution {
    static int diameter_1(Node root,int []res) {
        // Your code here
        if(root==null){
            return 0;
        }
        int lHeight=diameter_1(root.left,res);
        int rHeight=diameter_1(root.right,res);
        
        res[0]=Math.max(res[0],lHeight+rHeight);
        return 1+Math.max(lHeight,rHeight); 
        
    }
    static int diameter(Node root){
        
        int []res=new int[1];
        diameter_1(root,res);
        return res[0];
        
    }
}
