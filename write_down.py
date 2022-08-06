

def save_phone_number(book):
    path=r'telephon_book.txt'
    with open(path,'a') as data:
        data.write(f"{book[0]} : {book[1]} :{book[2]} : {book[3]} \n")
        
