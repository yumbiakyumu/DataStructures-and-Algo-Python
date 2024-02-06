"""Stack use case example"""
""" Storing a browser history """
""" When you go to a website eg https://edition.cnn.com/ and continue
to https://edition.cnn.com/us and then continue to https://edition.cnn.com/us/space-science all this data 
is saved in a stack """
""" When you hit the back arrow icon the last in is poped out ( https://edition.cnn.com/us/space-science) and the second in
( https://edition.cnn.com/us) page is show on the screen"""
""" Below is an implementation of the above stack"""


# s=[]
#pushing the web pages into the stack   
# s.append('https://edition.cnn.com/')
# s.append('https://edition.cnn.com/us')
# s.append('https://edition.cnn.com/us/space-science')
# s.append('https://edition.cnn.com/2024/01/26/us/cicadas-emergence-broods-xix-xiii-scn/index.html')

#to get the last page you visited you can use the pop method
#print(f'the last page you visited was {s.pop()}')

""" The pop however removes the element from the list 
so to avoid this you can use slicing  """
#print(f'The last page in the list is {s[-1]} ')

""" List have a challenge when implementing stacks
because they are dynamic arrays. So to implement
stack we can use deque from collections"""

# To implement stacks using deque
from collections import deque
# stk = deque()
#To append elements into the stack
# stk.append('https://edition.cnn.com/')
# stk.append('https://edition.cnn.com/us')
# stk.append('https://edition.cnn.com/us/space-science')
# stk.append('https://edition.cnn.com/2024/01/26/us/cicadas-emergence-broods-xix-xiii-scn/index.html')
# print(f"The stack has {stk}")

"""instead of repeating the line of code all the time
we can create a stack class and methods to do different
operations  """
class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,item):
        return self.container.append(item)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
    def print(self):
        return list(self.container)

stk=Stack()
stk.push(34)
stk.push(5768)
stk.push(3)
stk.push(4)
print(stk.print())