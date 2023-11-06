//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

#include <climits>
class Solution{
  public:
    int minDist(int arr[], int n, int x, int y) {
        // code here
        int ans=INT_MAX;
        int aa=-1,b=-1;
        for(int i=0;i<n;i++)
        {
            if(arr[i]==x)
            {
                aa=i;
            }
            if(arr[i]==y)
            {
                b=i;
            }
            if(aa!=-1 && b!=-1)
            {
                ans=min(ans,abs(aa-b));
            }
        }
        if(ans==INT_MAX || ans==0)
        {
            return -1;
        }
        else return ans;
    }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++) cin >> a[i];
        int x, y;
        cin >> x >> y;
        Solution obj;
        cout << obj.minDist(a, n, x, y) << endl;
    }
    return 0;
}

// } Driver Code Ends