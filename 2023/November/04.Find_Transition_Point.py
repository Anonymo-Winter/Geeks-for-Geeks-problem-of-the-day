class Solution:
    def transitionPoint(self, arr, n): 
        # Code here
        low = 0
        high = len(arr) - 1
    
        while low <= high:
            mid = (low + high) // 2
    
            if arr[mid] == 1:
                if mid == 0 or arr[mid - 1] == 0:
                    return mid
                high = mid - 1
            else:
                low = mid + 1
    
        return -1
        

#{ 
 # Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.transitionPoint(arr, n))

# } Driver Code Ends