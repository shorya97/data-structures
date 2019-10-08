class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=node(new_data)
        new_node.next=self.head
        self.head=new_data

    def deletenode(self,key):
        temp=self.head

        if (temp is not None):
            if (temp.data==key):
                self.head=temp.next
                temp=None
                return

        while(temp is not None):
            if temp.data==key:
                break
            prev=temp
            temp=temp.next

        if(temp==None):
            return

        prev.next=temp.next

        temp=None

    def printlist(self):
        temp=self.head
        while(temp):
           print ("temp.data")
           temp = temp.next


llist=linkedlist()
llist.push(2)
llist.push(4)
llist.push(8)

print("Created linked list: ")
llist.printlist()
llist.deletenode(8)
print("\n Linked List after deletion of 8 : ")
llist.printlist()



            
    
