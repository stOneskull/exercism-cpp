def total(books):
    booknum = len(books)
    bookvar = len(set(books))

    prices = {
    1:800, 2:1520, 3:2160, 4:2560, 5:3000
    }
    
    price = sum(
    prices[len(bookset)] for bookset in booksets(books)
    )
    
    return (
    price - booknum * 5
    if booknum % 8 == 0 and bookvar == 5
    else price 
    )
    

def booksets(books):
    while books:
        bookset = set(books)
        yield bookset
        for book in bookset:
            books.remove(book)
