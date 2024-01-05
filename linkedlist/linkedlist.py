class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
    """ Inserting a new node at the head of a linkedlist
        The time complexity is O(1)= This is because all you do is create
        a new node and modify the links 
     """
    def insert_at_beginning(self, data):
        # Create a new node with the given data
        node = Node(data,self.head)
        self.head = node
       
    #create a method t print out the linkedlist
    def print(self):
        #If the linked list is empty, it prints "Linked list is empty" and returns, indicating that there's nothing to print
        if self.head is None:
            print("Linked list is empty")
            return
        """if not empty, lkliststring = "" initializes an empty string to store the linked list representation.

           itr = self.head sets the iterator itr to the head of the linked list.

           The while itr: loop iterates through the linked list nodes.

           lkliststring += str(itr.data) + " ---> " concatenates the data of the current node to the existing lkliststring along with an arrow (--->) to represent the link.

           itr = itr.next moves the iterator to the next node.
        
        """
        
        itr=self.head
        lkliststring=''

        while itr:
            lkliststring+=str(itr.data) + "--->"
            itr = itr.next
        print(lkliststring)

if __name__ == '__main__':
    lnklst= Linkedlist()
    lnklst.insert_at_beginning(5)
    lnklst.insert_at_beginning(4)
    lnklst.insert_at_beginning(3)
    lnklst.insert_at_beginning(2)
    lnklst.insert_at_beginning(1)
   
    lnklst.print()

    
