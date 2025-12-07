

from abc import ABC, abstractmethod

class Tracker(ABC):
    @abstractmethod
    def run_once(self) -> None:
        ...