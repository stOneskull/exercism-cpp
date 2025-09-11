def total(books):
    items = len(books)
    unique = len(set(books))

    prices = {1: 800, 2: 1520, 3: 2160, 4: 2560, 5: 3000}

    price = sum(
    prices[len(bookset)] for bookset in booksets(books)
    )

    if items % 8 == 0 and unique == 5:
        # if there is a multiple of 8 books and
        # at least one of each of all 5 books
        # two sets of 4 = 5120, a 5 set and 3 set = 5160
        # the 8 books = 40c cheaper, 5c per book cheaper
        price -= items * 5
        
    return price 
    

def booksets(books):
    while books:
        bookset = set(books)
        yield bookset
        for book in bookset:
            books.remove(book)
