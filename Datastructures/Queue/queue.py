#CASE EXAMPLE"

""" New york Stock Exchange supplies stock price
changes to differernt Financial portals like 
Google Finance, Microsoft Finance etc. """

""" To do this they can implement an api that feeds
the finacial platforms HTTPS servers with Json objects
that contain the stock price informations."""

""" The problem with this is that if the server goes down
ther will be loss of messages and this infarstructure is tigthly 
coupled. To solve this a memory buffer like a queue can be used"""

""" Queues implement FIFO structure (First in First Out) whatever
is pushed in first is consumed first """
#implement a queue
# stock_price_queue = []
##to add elements at the beginning
# stock_price_queue.insert(0,135.90)
# stock_price_queue.insert(0,132.31)
# stock_price_queue.insert(0,137.84)
# #To remove an element you can use pop
# #But Queue are FIFO so 135.90 will be remove out
# print(stock_price_queue.pop())

""" List have a challenge when implementing Queues
because they are dynamic arrays. So to implement
Queues we can use deque from collections"""

from collections import deque
# q = deque()
# #To add an element to the queue
# q.appendleft(5)
# q.appendleft(35)
# q.appendleft(58)
# q.appendleft(8)
# print(q)
""" To make this easier we can create a class Queue
which contain the different methods used for queues"""
class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def print(self):
        return list(self.buffer)


q = Queue()

# Enqueue the stock information
q.enqueue({
    'company': 'Tesla',
    'date': '2024-01-01',
    'timestamp': '1640hrs',
    'stock_price': 123.34
})
q.enqueue({
    'company': 'Microsoft',
    'date': '2024-01-01',
    'timestamp': '1640hrs',
    'stock_price': 139
})
q.enqueue({
    'company': 'Nvidia',
    'date': '2024-01-01',
    'timestamp': '1640hrs',
    'stock_price': 145.36
})

# Dequeue each item separately and store them in variables
tesla_stock = q.dequeue()
microsoft_stock = q.dequeue()
nvidia_stock = q.dequeue()

# Print the stock information
print(f'Today is {tesla_stock["date"]}, the latest stock price of {tesla_stock["company"]} is ${tesla_stock["stock_price"]} at time {tesla_stock["timestamp"]}')
print(f'Today is {microsoft_stock["date"]}, the latest stock price of {microsoft_stock["company"]} is ${microsoft_stock["stock_price"]} at time {microsoft_stock["timestamp"]}')
print(f'Today is {nvidia_stock["date"]}, the latest stock price of {nvidia_stock["company"]} is ${nvidia_stock["stock_price"]} at time {nvidia_stock["timestamp"]}')

#Expected output
"""
Today is 2024-01-01, the latest stock price of Tesla is $123.34 at time 1640hrs
Today is 2024-01-01, the latest stock price of Microsoft is $139 at time 1640hrs
Today is 2024-01-01, the latest stock price of Nvidia is $145.36 at time 1640hrs 
"""
    
