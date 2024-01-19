from project.bookstore import Bookstore
import unittest


class BookstoreTest(unittest.TestCase):
    def setUp(self) -> None:
        self.store = Bookstore(3)

    def test_initialization(self):
        self.assertEqual(3, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_book_limit_error_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.store.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ex.exception))
        self.assertEqual(3, self.store.books_limit)

    def test_book_limit_error_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.store.books_limit = -1

        self.assertEqual("Books limit of -1 is not valid", str(ex.exception))
        self.assertEqual(3, self.store.books_limit)

    def test_book_limit_correct(self):
        self.store.books_limit = 10
        self.assertEqual(10, self.store.books_limit)
        self.store.receive_book("Titanic", 3)
        self.store.receive_book("1984", 3)

        self.assertEqual(6, len(self.store))
        self.assertEqual({"Titanic": 3, "1984": 3}, self.store.availability_in_store_by_book_titles)

    def test_len_empty(self):
        self.assertEqual(0, len(self.store))

    def test_len_one_book(self):
        self.store.availability_in_store_by_book_titles["1984"] = 1
        self.assertEqual(1, len(self.store))

    def test_receive_book_error_limit(self):
        with self.assertRaises(Exception) as ex:
            self.store.receive_book("1984", 4)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))
        self.assertEqual(0, len(self.store))

    def test_receive_book_correct(self):
        res = self.store.receive_book("1984", 3)
        self.assertEqual("3 copies of 1984 are available in the bookstore.", res)
        self.assertEqual(3, len(self.store))

    def test_sell_book_error_missing(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("1984", 1)

        self.assertEqual("Book 1984 doesn't exist!", str(ex.exception))
        self.assertEqual(0, len(self.store))
        self.assertEqual(0, self.store.total_sold_books)

    def test_sell_book_error_not_enough(self):
        self.store.receive_book("1984", 1)

        with self.assertRaises(Exception) as ex:
            self.store.sell_book("1984", 2)

        self.assertEqual("1984 has not enough copies to sell. Left: 1", str(ex.exception))
        self.assertEqual(1, len(self.store))
        self.assertEqual(0, self.store.total_sold_books)

    def test_sell_book_correct(self):
        self.store.receive_book("1984", 2)
        res = self.store.sell_book("1984", 1)

        self.assertEqual(1, self.store.total_sold_books)
        self.assertEqual("Sold 1 copies of 1984", res)
        self.assertEqual(1, len(self.store))

        res = self.store.sell_book("1984", 1)

        self.assertEqual(2, self.store.total_sold_books)
        self.assertEqual("Sold 1 copies of 1984", res)
        self.assertEqual(0, len(self.store))

    def test_correct_str(self):
        self.store.receive_book("1984", 2)
        self.store.sell_book("1984", 1)
        self.assertEqual("Total sold books: 1\nCurrent availability: 1\n - 1984: 1 copies", str(self.store))


if __name__ == "__main__":
    unittest.main()
