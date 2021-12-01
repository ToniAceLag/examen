#Ejercicio 1:
def list_natural_numbers():
    sum = 0
    naturals = list()
    num = valid_number(0, "Introdueix un nombre natural o cero per sortir:")
    while num != 0:
        naturals.append(num)
        num = valid_number(0, "Introdueix un nombre natural o cero per sortir:")
    for x in naturals:
        sum += x
    print(sum)


#Ejercicio 2:
def menu(msg):
    print("//////////////////////////////")
    print(msg)
    print("//////////////////////////////")


#Ejercicio 3:
def h_library():
    book = int(input("Insert how many books you wanna add:"))
    isbn = list()
    title = list()
    author = list()
    editorial = list()
    year_of_publication = list()
    for i in range(book):
        isbn.append(input("Insert the ISBN of the book:"))
        title.append(input("Insert the title of the book:"))
        author.append(input("Insert the author name:"))
        editorial.append(input("Instert the editorial name:"))
        year_of_publication.append(int(input("Instert the year of release of the book:")))
        print("Every time you see this messages means that you are starting a new book:")
        i +=1
    diccionario = {
        "Title:": title,
        "Author:": author,
        "Year of release:": year_of_publication,
        "Editorial:":editorial,
        "ISBN:":isbn
    }
    print(diccionario)


def valid_number(val, msg):
    num = int(input(msg))
    while num < val:
        num = int(input(msg))
    return num



