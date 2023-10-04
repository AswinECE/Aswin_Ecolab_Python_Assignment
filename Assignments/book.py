class book:
    def _init_(self,id,title,author,price,rating):
        self.id=id
        self.title=title
        self.author=author
        self.price=price 
        self.rating=rating
class library:
    def _init_(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)

    def ID(self,ID):
        for book in self.books:
            if book.id==ID:
                print(f"{book.id},{book.title},{book.author},{book.price},{book.rating}")
        return None
    
    def Author(self,author_name):
        for book in self.books:
            if book.author==author_name:
                print(f"{book.id},{book.title},{book.author},{book.price},{book.rating}")
        return None
    
    def Rating(self,start,end):
        for book in self.books:
            if (book.rating>start and book.rating<end):
                print(f"{book.id},{book.title},{book.author},{book.price},{book.rating}")
        return None
    
    def Price(self,start,end):
        for book in self.books:
            if (book.price>start and book.price<end):
                print(f"{book.id},{book.title},{book.author},{book.price},{book.rating}")
        return None
    
    def info(self):
        for i in self.books:
            print(f"{i.id},{i.title},{i.author},{i.price},{i.rating}")

b1=book(3001,"The village birds","HP",200,4)
b2=book(3002,"Tom&Jerry","Aswin",100,5)
b3=book(3003,"DC Comics","ZS",250,3)
b4=book(3004,"Resident Evil","Leon",400,2)

l=library()
l.add_book(b1)
l.add_book(b2)
l.add_book(b3)
l.add_book(b4)
l.info()
l.ID(3002)
l.Author("HP")
l.Rating(3,5)
l.Price(150,300)