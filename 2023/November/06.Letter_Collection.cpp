{ Driver Code Starts
 Initial Template for C++

#include bitsstdc++.h
using namespace std;

 } Driver Code Ends
 User function Template for C++

class Solution{
public
    vectorint matrixSum(int n, int m, vectorvectorint mat, int q, vectorint queries[])
    {
        vectorintans;
        for(int i=0;iq;i++)
        {
            int hop=queries[i][0];
            int r=queries[i][1];
            int c=queries[i][2];
            if(hop==1)
            {
                int dx[]={-1,-1,-1, 0,0, 1,1,1};
                int dy[]={-1, 0, 1,-1,1,-1,0,1};
                int sum=0;
                for(int j=0;j8;j++)
                {
                    int nr=r+dx[j];
                    int nc=c+dy[j];
                    if(nc=0 && nr=0 && nrn && ncm)
                    {
                        sum+=mat[nr][nc];
                    }
                }
                ans.push_back(sum);
            }
            else
            {
                int dx[]={-2,-2,-2,-2,-2,-1,-1, 0,0, 1,1, 2, 2,2,2,2};
                int dy[]={-2,-1, 0, 1, 2,-2, 2,-2,2,-2,2,-2,-1,0,1,2};
                int sum=0;
                for(int j=0;j16;j++)
                {
                    int nr=r+dx[j];
                    int nc=c+dy[j];
                    if(nr = 0 && nc = 0 && nrn && ncm)
                    {
                        sum+=mat[nr][nc];
                    }
                }
                ans.push_back(sum);
            }
        }
        return ans;
    }
};

{ Driver Code Starts.

int main(){
    int t;
    cint;
    while(t--){
        int n, m, q, ty, i, j;
        cinnm;
        vectorvectorint mat(n, vectorint(m, 0));
        for(int i = 0;i  n;i++)
            for(int j = 0;j  m;j++)
                cinmat[i][j];
        cinq;
        vectorint queries[q];
        for(int k = 0;k  q;k++){
            cintyij;
            queries[k].push_back(ty);
            queries[k].push_back(i);
            queries[k].push_back(j);
        }
        
        Solution ob;
        vectorint ans = ob.matrixSum(n, m, mat, q, queries);
        for(int u ans)
            coutun;
    }
    return 0;
}
 } Driver Code Ends