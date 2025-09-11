def total(books):
    booknum = len(books)
    bookvar = len(set(books))
    
    price = sum(
    (0, 800, 1520, 2160, 2560, 3000)[booksetlength]
    for booksetlength in booksetlengths(books)
    )
    
    return (
    price - booknum * 5
    if booknum % 8 == 0 and bookvar == 5
    else price 
    )
    

def booksetlengths(books):
    while books:
        bookset = set(books)
        yield len(bookset)
        for book in bookset:
            books.remove(book)
