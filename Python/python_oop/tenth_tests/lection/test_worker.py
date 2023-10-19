class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker("Test", 100, 50)

    def test_init(self):
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(50, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_working_correctly(self):
        self.worker.work()
        self.assertEqual(100, self.worker.money)
        self.assertEqual(50 - 1, self.worker.energy)

    def test_worker_cant_work_zero_energy(self):
        lazy_worker = Worker("Test", 100, 0)

        self.assertEqual("Test", lazy_worker.name)
        self.assertEqual(100, lazy_worker.salary)
        self.assertEqual(0, lazy_worker.energy)
        self.assertEqual(0, lazy_worker.money)

        with self.assertRaises(Exception) as ex:
            lazy_worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

        self.assertEqual("Test", lazy_worker.name)
        self.assertEqual(100, lazy_worker.salary)
        self.assertEqual(0, lazy_worker.energy)
        self.assertEqual(0, lazy_worker.money)

    def test_worker_cant_work_negative_energy(self):
        lazy_worker = Worker("Test", 100, -50)

        self.assertEqual("Test", lazy_worker.name)
        self.assertEqual(100, lazy_worker.salary)
        self.assertEqual(-50, lazy_worker.energy)
        self.assertEqual(0, lazy_worker.money)

        with self.assertRaises(Exception) as ex:
            lazy_worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

        self.assertEqual("Test", lazy_worker.name)
        self.assertEqual(100, lazy_worker.salary)
        self.assertEqual(-50, lazy_worker.energy)
        self.assertEqual(0, lazy_worker.money)

    def test_resting(self):
        self.worker.rest()

        self.assertEqual(50 + 1, self.worker.energy)

    def test_representation(self):
        resulting = f'{self.worker.name} has saved {self.worker.money} money.'

        self.assertEqual(resulting, self.worker.get_info())


if __name__ == "__main__":
    unittest.main()
