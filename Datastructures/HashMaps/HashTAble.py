#create hash class
class HashTable:
    def __init__(self):
        self.size = 10
        self.arr = [[] for  i in range(self.size)]



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
    #def __setitem__(self,key,value):
        #h=self.hashfunc(key)
        #self.arr[h] = value
    """ to avoid collision we have to use 
    chaining method so the the add method syntax will have to 
    change because now we have an array inside each array"""
    def __setitem__(self, key, value):
        h = self.hashfunc(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))



    #create a get method
    """the get method is used to 
    retrieve the value associated with
    a given key from the hash table"""
    #def get(self,key):
        #h=self.hashfunc(key)
        #return self.arr[h]

    def __getitem__(self,key):
        h=self.hashfunc(key)
        for element in self.arr[h]:
            if element[0] == key:
                    return element[1]
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
        for index, element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][index]
    
ex = HashTable()

ex['march 6'] = 345
ex['march 6'] = 1
ex['march 10'] = 67
ex['march 34'] = 35
ex['march 17'] = 9
ex['march 12'] = 3402

print(ex.arr) 

print(ex['march 6'])