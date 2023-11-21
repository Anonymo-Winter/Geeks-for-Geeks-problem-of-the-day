#User function Template for python3

''' structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

class Solution:
    def findIntersection(self,a,b):
        dummy = Node()
        tail = dummy;
        dummy.next = None;
      
        ''' Once one or the other 
        list runs out -- we're done '''
        while (a != None and b != None):
            if (a.data == b.data):
                tail.next = push((tail.next), a.data);
                tail = tail.next;
                a = a.next;
                b = b.next;
             
            # advance the smaller list
            elif(a.data < b.data):
                a = a.next;
            else:
                b = b.next;    
        return (dummy.next);
def push(head_ref, new_data):
 
    ''' allocate node '''
    new_node = Node()
  
    ''' put in the data  '''
    new_node.data = new_data;
  
    ''' link the old list of the new node '''
    new_node.next = (head_ref);
  
    ''' move the head to point to the new node '''
    (head_ref) = new_node;    
    return head_ref
 
#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        n1,n2 = [int(x) for x in input().split()]
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        ob = Solution()
        result = ob.findIntersection(ll1.head,ll2.head)
        printList(result)
        print()

# } Driver Code Ends