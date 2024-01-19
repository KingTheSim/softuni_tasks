from abc import ABC, abstractmethod
import time


class Workable(ABC):
    @staticmethod
    @abstractmethod
    def work() -> None:
        pass


class Eatable(ABC):
    @staticmethod
    @abstractmethod
    def eat() -> None:
        pass


class Worker(Workable, Eatable):
    @staticmethod
    def work() -> None:
        print("I'm normal worker. I'm working.")

    @staticmethod
    def eat() -> None:
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Workable, Eatable):
    @staticmethod
    def work() -> None:
        print("I'm super worker. I work very hard!")

    @staticmethod
    def eat() -> None:
        print("Lunch break....(3 secs)")
        time.sleep(3)


class WorkManager:
    def __init__(self) -> None:
        self.worker = None

    def set_worker(self, worker: Workable) -> None or AssertionError:
        if isinstance(worker, Workable):
            self.worker = worker

        else:
            raise AssertionError(f"`worker` must be of type {Workable}")

    def manage(self) -> None:
        self.worker.work()


class BreakManager:
    def __init__(self) -> None:
        self.worker = None

    def set_worker(self, worker: Eatable) -> None or AssertionError:
        if isinstance(worker, Eatable):
            self.worker = worker

        else:
            raise AssertionError(f"`worker` must be of type {Eatable}")

    def lunch_break(self) -> None:
        self.worker.eat()


class Robot(Workable):
    @staticmethod
    def work() -> None:
        print("I'm a robot. I'm working....")


work_manager = WorkManager()
break_manager = BreakManager()

work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()

break_manager.lunch_break()
work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()

break_manager.lunch_break()
work_manager.set_worker(Robot())
work_manager.manage()

try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except AssertionError:
    pass
