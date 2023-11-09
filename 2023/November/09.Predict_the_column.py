#User function Template for python3

class Solution:
    
    def columnWithMaxZeros(self,arr,N):
        # code here
        index=-1
        list=[]
        cnt=0
        temp=0
        while(temp<N):
            cnt=0
            for i in range(0,N):
                if(arr[i][temp]==0):
                    cnt+=1
            if(cnt==N):
                return temp
            list.append(cnt)
            temp+=1
        ans=max(list)
        return -1 if ans==0 else list.index(ans)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = []
        for i in range(N):
            line = [int(x) for x in input().strip().split()]
            arr.append(line)
        ob=Solution()
        print(ob.columnWithMaxZeros(arr,N))


# } Driver Code Ends