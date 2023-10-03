class Node:
    def __init__(self, value,next=None, previous=None):
        self._value=value
        self._next=next
        self._previous=previous

class LinkedList:
    def __init__(self):
        self._first=None

    def append(self, value):
        if self._first==None:
            self._first=Node(value)
        else:
            n=self._first
            while n._next:
                n=n._next
            n._next=Node(value, previous=n)

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
    
def loop(list,index):
    count = 0
    prev = list._first
    cur = list._first
    while count<index and cur:
        prev = cur            
        cur = cur._next                
        count+=1
    return [prev,cur]

def isprime(n):
    flag = 0
    for i in range(2,int((n)/2+1)):
        if n%i==0:
            flag=1
    if flag == 0:
        return 1
    else:
        return 0


def Findprime(list):
    print("PRIME NUMBERS")
    cur = list._first
    prev = list._first
    while cur._next:
        prev = cur            
        cur = cur._next      
        data = cur._value
        if(isprime(data) and data!=1 and data!=0):
            print(data," ")  

def isEven(list):
    print("\nEVEN NUMBERS")
    cur = list._first
    prev = list._first
    while cur._next:
        prev = cur            
        cur = cur._next      
        data = prev._value  
        if data%2==0:
            print(f'{data}', " ")

list1 = LinkedList()
for i in range(30):
    list1.append(i)
Findprime(list1)

isEven(list1)