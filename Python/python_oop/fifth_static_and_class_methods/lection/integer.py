class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: str):
        try:
            return cls(int(float_value))
        except ValueError:
            return "value is not a float"

    @classmethod
    def from_roman(cls, value: str):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        summ = 0
        for i in range(len(value) - 1, -1, -1):
            num = roman[value[i]]
            if 3 * num < summ:
                summ = summ - num
            else:
                summ = summ + num
        return cls(summ)

    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, str):
            return "wrong type"
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"


import unittest


class IntegerTests(unittest.TestCase):
    def test_basic_init(self):
        integer = Integer(1)
        self.assertEqual(integer.value, 1)

    def test_from_float_success(self):
        integer = Integer.from_float(2.5)
        self.assertEqual(integer.value, 2)

    def test_from_float_wrong_type(self):
        result = Integer.from_float("2.5")
        self.assertEqual(result, "value is not a float")

    def test_from_roman(self):
        integer = Integer.from_roman("XIX")
        self.assertEqual(integer.value, 19)

    def test_from_string_success(self):
        integer = Integer.from_string("10")
        self.assertEqual(integer.value, 10)

    def test_from_string_wrong_type(self):
        result = Integer.from_string(1.5)
        self.assertEqual(result, "wrong type")


if __name__ == "__main__":
    unittest.main()

