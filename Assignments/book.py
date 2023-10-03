class BookNode:
    def __init__(self,id,title,author,price,rating,next=None, previous=None):
        self._id = id
        self._title = title
        self._author = author
        self._price = price
        self._rating = rating
        self._next=next
        self._previous=previous

class Book:
    def __init__(self):
        self._first=None

    def append(self,id,title,author,price,rating):
        if self._first==None:
            self._first=BookNode(id,title,author,price,rating)
        else:
            n=self._first
            while n._next:
                n=n._next
            n._next=BookNode(id,title,author,price,rating, previous=n)

    def info(self):
        if self._first==None: 
            return "LinkedList(empty)"
        str="LinkedList(\t"
        n=self._first
        while n:
            str+=f'{n._title}\t'
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
    
b = Book()
print(b.info())
b.append(123,"YSR","ARR",50,5)
print(b.info())

def ID(list,id):
    cur = list._first
    while cur:
        if cur._id==id:
            return f'{cur._title}'
        cur = cur._next
    else:
        return f'Id not found'
     
ID(b,123)

def BookAuthor(list,author):
    cur = list._first
    flag=0
    while cur:
        if cur._author==author:
            flag=1
            print( f'{cur._title}')
        cur = cur._next
        
    else:
        if flag==0:
            return f'No author by {author} found'

BookAuthor(b,"ARR")

def BookRating(list,rating):
    cur = list._first
    flag=0
    while cur:
        if cur._rating==rating:
            flag = 1
            print( f'{cur._title}')
        cur = cur._next
        
    else:
        if flag==0:
            return f'No book has rating {rating}'

BookRating(b,5)

def BookPrice(list,min,max):
    cur = list._first
    flag=0
    while cur:
        if cur._price<max and cur._price>min:
            flag = 1
            print( f'{cur._title}')
        cur = cur._next
        
    else:
        if flag==0:
            return f'No book has within the prce range{min,max}'
        
BookPrice(b,25,50)
