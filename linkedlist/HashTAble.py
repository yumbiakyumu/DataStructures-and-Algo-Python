#create hash class
class HashTable:
    def __init__(self):
        self.size = 100
        self.arr = [None for i in range(self.size)]



#create a hash function
    """
    The hashfunc function takes a string (key), 
    iterates through each character in the string,
    and accumulates their ASCII values to compute
    a hash value. The hash value is then 
    returned after applying modulo 100 
    to keep it within a specific range.

    """
    def hashfunc(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.size

    #create an add method
    """ the add method is used to add key-value 
    pairs to the hash table"""
    #def add(self,key,value):
        #h=self.hashfunc(key)
        #self.arr[h] = value
    def __setitem__(self,key,value):
        h=self.hashfunc(key)
        self.arr[h] = value


    #create a get method
    """the get method is used to 
    retrieve the value associated with
     a given key from the hash table"""
    #def get(self,key):
        #h=self.hashfunc(key)
        #return self.arr[h]

    def __getitem__(self,key):
        h=self.hashfunc(key)
        return self.arr[h]    
    """
    Python has in built functions that eanble 
    you to call the "add" and the "get" method
    without repeating all the  for this you
    replace def get() with def __getitem__() and 
    def  add() with def __setitem__()
    so in short you can do this 
    to add ex['march 6'] = 10
    To get the value you can do this
     print ex['march 6']

    """
    #delete element by key
    """The delete method removes the pair of
    key/value associated with the input key."""
    def __delitem__(self,key):
        h=self.hashfunc(key)
        self.arr[h] = None
    
ex = HashTable()
ex['march 30'] = 234
ex['march 5'] = 23
ex['march 3'] = 24
ex['Dec 30'] = 3456
ex['march 20'] = 234

#print(ex.arr)

del ex['Dec 30']
print(ex['Dec 30'])

