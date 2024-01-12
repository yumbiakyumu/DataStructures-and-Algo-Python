class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

class DoublyLinkedlist:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("List is empty")
            return

        itr = self.head
        l_str=''
        while itr:
            l_str += str(itr.data)+" --> "
            itr = itr.next

        print(l_str)

    def insert_at_beginning(self,data):
        if self.head is None:
            new_node = Node(data, self.head, None)
            self.head = new_node
        else:
            new_node = Node(data,self.head,None)
            self.head.prev = new_node
            self.head = new_node

    def get_last_node(self):
        itr = self.head
        last=''
        while itr and itr.next:   
            itr = itr.next
        last+=str(itr.data)
        print(last)
        return itr    
            
        

    def print_backwards(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        last_node=self.get_last_node()
        itr = last_node
        bck=''
        while itr:
           bck+=str(itr.data) + '<--'
           itr = itr.prev
        print("The linked list printed backwards:",bck)

    def getLength(self):
        count=0
        
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        #print(count)
        return count

    def insert_at_end(self, data):
        if self.head is None:
            self.head= Node(data, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert(self, data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        if index<0 or index>self.getLength():
          raise Exception("Invalid Index")
          

        if index == 0:
            self.insert_at_beginning(data)
            return

        count=0
        itr=self.head
        while itr:
            if count == index - 1:
                newNode = Node(data,itr.next,itr)

            if node.next:
                node.next.prev=newNode
            itr.next = Node
            break
            itr = itr.next
            count += 1
    

if __name__ == '__main__':
    dll = DoublyLinkedlist()
    #dll.insert_at_beginning(12)
    #dll.insert_at_beginning(10)
    #dll.insert_at_beginning(9)
    #dll.print_forward()
    #dll.get_last_node()
    #dll.print_backwards() 
    #dll.getLength()
    dll.insert(["Gordons","Hennessey","Morgans","Juice","Maji"])
    dll.print_forward()
    dll.insert_at(0, "Meakins")
    dll.print_forward()

