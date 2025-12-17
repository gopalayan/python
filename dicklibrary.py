library={}
def add_book(title,author,year):
    library[title]={"author":author,"year":year}
    print(f"{library [title]} this book added" )
def search(title):
    book=library[title]    
    print(book)
while(True):
    print("1 for add book")
    print("2 for search book") 
    ch=int(input("enter ur number :"))
    if ch==1:
        title=input("enter your title: ")
        author=input("enter your author: ")
        year=int(input("enter your year:"))
        add_book(title,author,year) 
    if ch==2:
        title=input("enter your title: ")
        search(title)      