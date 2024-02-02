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

    #inserting element at the end
  
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data , None)
    #Inserting new value into the linkedlist
    def insert(self, data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
    #finding length of LinkedList
    def getLength(self):
        count=0
        itr=self.head
        while itr:
            count +=1
            itr=itr.next

        return count
    # remove element from given index
    def remove_at(self,index):
        if index<0 or index>=self.getLength():
            raise Exception("Index out of range")
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1
    #Inserting element and value at given index
    def insert_at(self, index, data):
        if index < 0 or index > self.getLength():
            raise Exception("Index out of range")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after,data_to_insert):
        itr = self.head
        while itr :
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                return
                itr = itr.next
            
        raise ValueError('The specified value does not exist in the list')

    def remove_by_value(self,data):
        itr = self.head
        if itr.data == data:
            self.remove_from_index(0)
            return
        else:
            while itr.next:
                if itr.next.data==data:
                    itr.next=itr.next.next
                    itr=itr.next
                    return
                itr=itr.next
            raise ValueError('The specified value is not found in the list')
    
            


       







if __name__ == '__main__':
    lnklst= Linkedlist()
   
    #lnklst.insert(["ford","Toyota","Hyundai","Subaru"])
    #lnklst.remove_at(2)
    #lnklst.print()
    #print("The length of the linked list",lnklst.getLength())
    #lnklst.insert_at(0, "Honda")
    lnklst.insert(["banana","mango","grapes","orange"])
    lnklst.print()
    #lnklst.insert_after_value("mango","apple")
    lnklst.remove_by_value("orange")
    lnklst.print()

    
