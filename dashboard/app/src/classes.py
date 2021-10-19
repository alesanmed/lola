from abc import ABC, abstractmethod


class Page(ABC):
    @abstractmethod
    def write(self):
        pass
