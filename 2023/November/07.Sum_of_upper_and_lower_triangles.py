
#User function Template for python3


class Solution:
    # example 
        # 1[No.of Test Case]
        # 3 [=N]
        # 1 2 3 4 5 6 7 8 9 {N*N} Matrix
    def sumTriangles(self,arr, n):
        sum1=0
        sum2=0
        for i in range(n):
            for j in range(n):
                if(i<=j): sum1+=arr[i][j]
                if(i>=j):
                    sum2+=arr[i][j]
        ans=[]
        ans.append(sum1)
        ans.append(sum2)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]

        k=0 
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        ans = obj.sumTriangles(matrix, n)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends