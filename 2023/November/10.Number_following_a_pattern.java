//{ Driver Code Starts
import java.io.*;
import java.util.*;

public class GFG
{
    public static void main(String args[])throws IOException
    {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while(t-- > 0)
        {
            String S = read.readLine();
            Solution ob = new Solution();
            System.out.println(ob.printMinNumberForPattern(S));
        }
    }
}
// } Driver Code Ends


//User function Template for Java
class Solution{
    static String printMinNumberForPattern(String S){
     Stack<String> stack=new Stack<>();
     String s="";
     for(int i=0; i<=S.length();i++)
     {
         String k=String.valueOf(i+1);
         stack.push(k);
         if(i==S.length() || S.charAt(i)=='I')
         {
             while(!stack.isEmpty())
             {
                 s+=stack.pop();
             }
         }
     }
     return s;
    }
}

