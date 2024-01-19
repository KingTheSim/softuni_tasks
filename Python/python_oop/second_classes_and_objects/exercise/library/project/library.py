from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if author in self.books_available:
            if book_name in self.books_available[author]:
                self.books_available[author].remove(book_name)

                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {}

                self.rented_books[user.username][book_name] = days_to_return
                user.books.append(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"

        days = 0
        for u in self.rented_books:
            if book_name in u:
                days = self.rented_books[u][book_name]
        return f'The book "{book_name}" is already rented' \
               f' and will be available in {self.rented_books[user.username][book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User) -> None or str:
        if user.username in self.rented_books:
            if book_name in self.rented_books[user.username]:
                self.books_available[author].append(book_name)
                self.rented_books[user.username].pop(book_name)
                user.books.remove(book_name)

            else:
                return f"{user.username} doesn't have this book in his/her records!"

        else:
            return f"{user.username} doesn't have this book in his/her records!"
