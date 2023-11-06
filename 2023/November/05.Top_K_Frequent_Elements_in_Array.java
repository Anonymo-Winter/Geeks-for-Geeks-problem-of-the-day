//{ Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;
class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while (T-- > 0) {
            String[] s = br.readLine().trim().split(" ");
            int n = Integer.parseInt(s[0]);
            int[] nums = new int[n];
            for (int i = 0; i < n; i++) {
                nums[i] = Integer.parseInt(s[i + 1]);
            }
            int k = Integer.parseInt(br.readLine().trim());
            Solution obj = new Solution();
            int[] ans = obj.topK(nums, k);
            for (int i = 0; i < ans.length; i++) System.out.print(ans[i] + " ");
            System.out.println();
        }
    }
}

// } Driver Code Ends


class Solution {
    public int[] topK(int[] nums, int k) {
        // Code here

        int[] result = new int[k];
        Map<Integer, Integer> frequencies = new HashMap<>();
        for(int x : nums) {
            frequencies.put(x, frequencies.getOrDefault(x, 0) + 1);
        }
        
        PriorityQueue<Map.Entry<Integer, Integer>> frequentList = new PriorityQueue<>(k, new Compare());
        for(Map.Entry<Integer, Integer> entry: frequencies.entrySet()) {
            frequentList.add(entry);
            
            if(frequentList.size() > k) {
                frequentList.poll();
            }
        }
    
        while(!frequentList.isEmpty()) {
            Map.Entry<Integer, Integer> frequentEntry = frequentList.poll();
            result[--k] = frequentEntry.getKey();
        }
        
        return result;
    }
}
class Compare implements Comparator<Map.Entry<Integer, Integer>>
{
    public int compare(Map.Entry<Integer, Integer> o1, Map.Entry<Integer, Integer> o2) {
        if(o1.getValue() == o2.getValue()) {
            return o1.getKey() - o2.getKey();
        }
        
        return o1.getValue() - o2.getValue();
    }
}
        