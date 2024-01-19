from abc import ABC, abstractmethod


class WorkerTemplate(ABC):
    @staticmethod
    @abstractmethod
    def work() -> None:
        pass


class Worker(WorkerTemplate):
    @staticmethod
    def work() -> None:
        print("I'm working!!")


class Manager:

    def __init__(self) -> None:
        self.worker = None

    def set_worker(self, worker) -> None or AssertionError:
        if isinstance(worker, WorkerTemplate):
            self.worker = worker

        else:
            raise AssertionError(f"`worker` must be of type {WorkerTemplate}")

    def manage(self) -> None:
        if self.worker is not None:
            self.worker.work()


class SuperWorker(WorkerTemplate):
    @staticmethod
    def work() -> None:
        print("I work very hard!!!")


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()
super_worker = SuperWorker()

try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
