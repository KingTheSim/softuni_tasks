class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.list = IntegerList(1, 2, 3, 4, "5")

    def test_initialization(self):
        self.assertEqual([1, 2, 3, 4], self.list.get_data())
        self.assertEqual(4, len(self.list.get_data()))

    def test_no_integers_case(self):
        cur_list = IntegerList(1.1, "2", "three", False)
        self.assertEqual(0, len(cur_list.get_data()))

    def test_cant_add(self):
        with self.assertRaises(ValueError) as ex:
            self.list.add("a")

        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual(4, len(self.list.get_data()))

    def test_can_add(self):
        cur = self.list.add(5)

        self.assertIn(5, cur)
        self.assertEqual(5, len(cur))
        self.assertEqual([1, 2, 3, 4, 5], cur)

    def test_cant_remove_index_equal(self):
        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(4)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(4, len(self.list.get_data()))

    def test_cant_remove_index_higher(self):
        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(5)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(4, len(self.list.get_data()))

    def test_can_remove_index(self):
        cur = self.list.remove_index(0)

        self.assertNotIn(1, cur)
        self.assertEqual(3, len(cur))
        self.assertEqual([2, 3, 4], cur)

    def test_cant_get_equal(self):
        with self.assertRaises(IndexError) as ex:
            self.list.get(4)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_cant_get_higher(self):
        with self.assertRaises(IndexError) as ex:
            self.list.get(5)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_can_get(self):
        cur = self.list.get(0)

        self.assertEqual(1, cur)

    def test_cant_insert_index_equal(self):
        with self.assertRaises(IndexError) as ex:
            self.list.insert(4, 5)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(4, len(self.list.get_data()))
        self.assertEqual([1, 2, 3, 4], self.list.get_data())

    def test_cant_insert_index_higher(self):
        with self.assertRaises(IndexError) as ex:
            self.list.insert(5, 5)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(4, len(self.list.get_data()))
        self.assertEqual([1, 2, 3, 4], self.list.get_data())

    def test_cant_insert_type_error(self):
        with self.assertRaises(ValueError) as ex:
            self.list.insert(4, "5")

        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual(4, len(self.list.get_data()))
        self.assertEqual([1, 2, 3, 4], self.list.get_data())

    def test_can_insert(self):
        self.list.insert(1, 5)

        self.assertEqual(5, len(self.list.get_data()))
        self.assertEqual([1, 5, 2, 3, 4], self.list.get_data())

    def test_get_largest(self):
        cur = self.list.get_biggest()

        self.assertEqual(4, cur)

    def test_cant_get_index(self):
        with self.assertRaises(ValueError) as ex:
            self.list.get_index(60)

        self.assertEqual("60 is not in list", str(ex.exception))

    def test_can_get_index(self):
        cur = self.list.get_index(1)

        self.assertEqual(0, cur)


if __name__ == "__main__":
    unittest.main()
