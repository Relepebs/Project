class TAX():
    def __int__ (self):

        self._list = 0
        self._author = "n"
        self._name = "n"
        self.books = {}
        self._price = float(0)

    def add(self):
        self._name= input("Enter book name:")
        self._author= input("Author:")
        self._price= input("Price:$")
        print(self._name)
        self.books[self._name] = {self._author, self._price}
        print(self.books)

    def sell(self):
        self._name = input("Name of book to sell:")
        self._price = input("Price:$")
    