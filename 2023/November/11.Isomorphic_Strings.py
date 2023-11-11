#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        if(len(str1)!=len(str2)):
            return False
        s1=[-1]*256
        s2=[-1]*256
        for i in range(len(str1)):
            c1=str1[i]
            c2=str2[i]
            if(s1[ord(c1)]==-1 and s2[ord(c2)]==-1):
                s1[ord(c1)]=c2
                s2[ord(c2)]=c1
            elif(s1[ord(c1)]!=c2 or s2[ord(c2)]!=c1):
                return False
        return True
            
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends