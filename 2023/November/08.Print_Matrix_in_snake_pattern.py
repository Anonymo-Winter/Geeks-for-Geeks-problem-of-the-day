
#User function Template for python3

class Solution:
    
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix):
        n=len(matrix)
        list=[]
        row=0
        
        while(row<n):
            if(row%2==0):
                for i in range(0,n):
                    list.append(matrix[row][i])
            else:
                for i in range(n-1,-1,-1):
                    list.append(matrix[row][i])
            
            row+=1
        return list
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.snakePattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends
