class Author:
    all = []

    def __init__(self, name: str):
        self.name = name
        self._contracts = []
        Author.all.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book: 'Book', date: str, royalties: int):
        if not isinstance(book, Book):
            raise Exception("book is not of class Book")

        if not isinstance(date, str):
            raise Exception("date is not a string")

        if not isinstance(royalties, int):
            raise Exception("royalties is not an integer")

        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)

    def add_contract(self, contract: 'Contract'):
        if not isinstance(contract, Contract):
            raise Exception("contract not of class Contract")
        self._contracts.append(contract)


class Book:
    all = []

    def __init__(self, title: str):
        self.title = title
        self._contracts = []
        Book.all.append(self)

    def contracts(self):
        return self._contracts

    def authors(self):
        return list(set(contract.author for contract in self._contracts))


class Contract:
    all = []

    def __init__(self, author: 'Author', book: 'Book', date: str, royalties: int):
        if not isinstance(author, Author):
            raise Exception("author is not of class Author")

        if not isinstance(book, Book):
            raise Exception("book is not of class Book")

        if not isinstance(date, str):
            raise Exception("date is not a string")

        if not isinstance(royalties, int):
            raise Exception("royalties is not an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)
        author._contracts.append(self)
        book._contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date: str):
        if not isinstance(date, str):
            raise Exception("date is not a string")
        return [contract for contract in cls.all if contract.date == date]
