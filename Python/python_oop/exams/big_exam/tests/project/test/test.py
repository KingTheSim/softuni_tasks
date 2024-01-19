from project.second_hand_car import SecondHandCar
import unittest


class SecondHandCarTest(unittest.TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("Toyota", "Sport", 101, 2.0)

    def test_initialization_correct(self):
        self.assertEqual("Toyota", self.car.model)
        self.assertEqual("Sport", self.car.car_type)
        self.assertEqual(101, self.car.mileage)
        self.assertEqual(2.0, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_error_one(self):
        with self.assertRaises(ValueError) as ex:
            self.car.price = 1.0

        self.assertEqual('Price should be greater than 1.0!', str(ex.exception))
        self.assertEqual(2.0, self.car.price)

    def test_price_error_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.car.price = 0.0

        self.assertEqual('Price should be greater than 1.0!', str(ex.exception))
        self.assertEqual(2.0, self.car.price)

    def test_price_correct_change(self):
        self.car.price = 3.0
        self.assertEqual(3.0, self.car.price)

    def test_mileage_error_one_hundred(self):
        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 100

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ex.exception))
        self.assertEqual(101, self.car.mileage)

    def test_mileage_error_50(self):
        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 50

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ex.exception))
        self.assertEqual(101, self.car.mileage)

    def test_mileage_correct_change(self):
        self.car.mileage = 103
        self.assertEqual(103, self.car.mileage)

    def test_set_promotional_price_error_equal(self):
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(2.0)

        self.assertEqual('You are supposed to decrease the price!', str(ex.exception))
        self.assertEqual(2.0, self.car.price)

    def test_set_promotional_price_error_greater(self):
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(3)

        self.assertEqual('You are supposed to decrease the price!', str(ex.exception))
        self.assertEqual(2.0, self.car.price)

    def test_set_promotional_price_correct(self):
        res = self.car.set_promotional_price(1.5)
        self.assertEqual(1.5, self.car.price)
        self.assertEqual('The promotional price has been successfully set.', res)

    def test_need_repair_error_too_high(self):
        res = self.car.need_repair(3, "test")
        self.assertEqual('Repair is impossible!', res)
        self.assertEqual(2.0, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_need_repair_correct(self):
        res = self.car.need_repair(1, "test")
        self.assertEqual("Price has been increased due to repair charges.", res)
        self.assertEqual(3, self.car.price)
        self.assertEqual(["test"], self.car.repairs)
        new_res = self.car.need_repair(1, "test1")
        self.assertEqual("Price has been increased due to repair charges.", new_res)
        self.assertEqual(4, self.car.price)
        self.assertEqual(["test", "test1"], self.car.repairs)

    def test_gt_same_type_higher_price(self):
        self.car1 = SecondHandCar('Toyota Corolla', 'Sedan', 3000, 15000.0)
        self.car3 = SecondHandCar('Ford Fusion', 'Sedan', 6000, 20000.0)
        self.assertTrue(self.car3 > self.car1)

    def test_gt_same_type_lower_price(self):
        self.car1 = SecondHandCar('Toyota Corolla', 'Sedan', 3000, 15000.0)
        self.car3 = SecondHandCar('Ford Fusion', 'Sedan', 6000, 20000.0)
        self.assertFalse(self.car1 > self.car3)

    def test_gt_different_type(self):
        self.car1 = SecondHandCar('Toyota Corolla', 'Sedan', 3000, 15000.0)
        car4 = SecondHandCar('Nissan Rogue', 'SUV', 4000, 21000.0)
        result = self.car1 > car4
        self.assertEqual(result, 'Cars cannot be compared. Type mismatch!')

    def test_str_method(self):
        self.car1 = SecondHandCar('Toyota Corolla', 'Sedan', 3000, 15000.0)
        self.car2 = SecondHandCar('Honda CR-V', 'SUV', 8000, 18000.0)

        expected_output1 = "Model Toyota Corolla | Type Sedan | Milage 3000km\nCurrent price: 15000.00 | Number of Repairs: 0"
        expected_output2 = "Model Honda CR-V | Type SUV | Milage 8000km\nCurrent price: 18000.00 | Number of Repairs: 0"

        self.assertEqual(str(self.car1), expected_output1)
        self.assertEqual(str(self.car2), expected_output2)
