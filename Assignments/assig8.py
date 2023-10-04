class Node:
    def _init_(self, value,_next=None, previous=None):
        self._value=value
        self._next=_next
        self._previous=previous
class LinkedList:
    def _init_(self):
        self._first=None
        self._last=None

    def append(self, value):
        if self._first==None: # list is empty
            newN = Node(value)
            self._first=newN
            self._last=newN
        else: # add to the end of a non-empty list
            n=self._first
            while n._next:
                n=n._next
            newN=Node(value, previous=n)
            n._next=newN
            self._last=newN

    # Optimize Code to append data
    def append_last(self,value):
        if self._first==None: # list is empty
            newN = Node(value)
            self._first=newN
            self._last=newN
        else: # add to the end of a non-empty list
            newN=Node(value,previous=self._last)
            self._last._next=newN
            self._last=newN
            print(self._last._value)

    #Optimizing Code to accessing the items
    def get_first(self):
        first = self._first._value if self._first else None
        print(f'first : {first} ')

    def get_last(self):
        last = self._last._value if self._last else None
        print(f'last: {last}')

    #Otimized code to remove 
    def remove_opt(self):
        self._first = None
        self._last = None
    
    #optimized
    def count(self, value):
        cur = self._first 
        count = 0
        while(cur != None):
            if(cur._value == value):
                count += 1
            cur = cur._next
        return count



    def info(self):
        if self._first==None: 
            return "LinkedList(empty)"
        str="LinkedList(\t"
        n=self._first
        while n:
            str+=f'{n._value}\t'
            n=n._next
        str+=")"
        return str

    def size(self):
        c=0
        n=self._first
        while n:
            c+=1
            n=n._next
        return c
            
l1 = LinkedList()

print(l1.info())

for value in [2,3,9,2,6]:
    l1.append(value)

print('size', l1.size())
print(l1._last._value)
l1.append_last(10)
print(l1.info())


def get(list,index):
    n=list._first
    for i in range(index):
        n=n._next
        if n==None:
            break
    else:
        return n._value

LinkedList.get = get
l1.get(3)

def set(list,index,value):
    n=list._first
    for i in range(index):
        n=n._next
        if n==None:
            break
    else:
        n._value=value

LinkedList.set=set
l2=LinkedList()
for i in range(5):
    l2.append(i)
    
for i in range(l2.size()):
    print(l2.get(i))
    l2.set(i, i*10)

print(l2.info())


def loop(list,index):
    count = 0
    prev = list._first
    cur = list._first
    while count<index and cur:
        prev = cur            
        cur = cur. _next                
        count+=1
    return [prev,cur]
def insert(list, index, value):
    # print(list.size())
    if (index > list.size()) or index<0:
        print("Invalid INdex")

    else:
    
        if index == 0:
            newN = Node(value,list._first,None)
            list._prev = newN
            list._first = newN


        else:
            prev,cur = loop(list,index)
            # print(cur._value)
            print(prev._value)
            if index == list.size():
                newN = Node(value,None,prev)
                prev. _next = newN
            else:
                newN = Node(value,cur,prev)
                cur._previous = newN
                prev. _next = newN

        
    

def remove(list, index):
    if (index > list.size()) or index<0:
        print("Invalid INdex")

    else:
    
        if index == 0:
            list._first = list._first. _next
            list._first._previous = None


        else:
            prev,cur = loop(list,index)
            print(cur._value)
            print(prev._value)
            if index == list.size()-1:
                 prev. _next = None
            else:
                  prev. _next = cur. _next
                  cur. _next._prev = prev 
remove(l2,3)
print(l2.info())
