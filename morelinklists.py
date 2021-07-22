
# remove duplicate in linklists
# ex: input 1 2 2 3 3 4 
# output : 1 2 3 4

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        current = head
        if current is not None and current.next == None:
            #print("Empty")
            return current
        elif current.next is not None:
            
            while (current and current.next is not None):
                nextnode = current.next
                #print("nextnode",nextnode.data)
                #print("current",current.data)
                if current.data == nextnode.data:
                    #print("Remove", current.data)
                    nextnextnode = nextnode.next
                    current.next = nextnextnode
                    nextnode.next = None
                
                else:
                    current = current.next
                
            return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 