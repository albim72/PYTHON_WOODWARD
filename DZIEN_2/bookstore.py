class Book:
    __kolor = "czerwony"
    def __init__(self,title,author,price,pages,bookstore_nb):
        self.title = title
        self.author = author
        self._price = price
        self.pages = pages
        self.bookstore_nb = bookstore_nb
        self.binding = "miękka"

    def __repr__(self):
        return f"Ksiażka: {self.title}, cena -> {self.price} zł"

    def __call__(self, procent):
        return f"Książka, oprawa {self.binding}, kolor: {self.__kolor}, rabat {procent} %  -> do zapłaty: {(1-procent/100)*self.price:.2f} zł"

    def get_bind(self):
        return self.binding

    def set_bind(self,newbind):
        self.binding = newbind

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,newtitle):
        self._title = newtitle

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,newprice):
        self._price = newprice



b = Book("ABC Kulturysty","Jan Nowak",56.6,456,34)
print(b)
print(b(12))

b.binding = "twarda"
print(b(23))

print(b.title)
b.title = "ABC Młodego Kulturysty"
print(b.title)

