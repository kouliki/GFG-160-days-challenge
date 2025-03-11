class Solution {
  public:
    int kthMissing(vector<int> &arr, int k) {
        // Your code goes here
        
        int num=1;
        int n=arr.size();
        int i=0;
        
        while(k>0 && i<n)
        {
            if (arr[i]==num)  // when number found
            {
               i++;
            }
            else{
                k--;
            }
            num++;
        }
        
        // edge cases [1,2,3]
        
        while(k--){
            num++;
        }
        return num-1;
        
    }
};

//{ Driver Code Starts.

int main() {
    int test_case;
    cin >> test_case;
    cin.ignore();
    while (test_case--) {

        int d;
        vector<int> arr, brr, crr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        getline(cin, input);
        ss.clear();
        ss.str(input);
        while (ss >> number) {
            crr.push_back(number);
        }
        d = crr[0];
        int n = arr.size();
        Solution ob;
        int ans = ob.kthMissing(arr, d);
        cout << ans << endl;

        cout << "~"
             << "\n";
    }
    return 0;
}
// } Driver Code Ends
