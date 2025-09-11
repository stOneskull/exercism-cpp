def calculate_total(books):
    booknum = len(books)
    price = sum(
    (0,800,1520,2160,2560,3000)[len(bookset)]
    for bookset in get_sets(books)
    )
    return price if booknum % 8 else price - booknum * 5


def get_sets(books):
    while books:
        bookset = set(books)
        yield bookset
        for book in bookset:
            books.remove(book)
