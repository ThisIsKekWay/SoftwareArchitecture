from abc import ABC, abstractmethod
from IModelChangedObserver import IModelChangedObserver


class IModelChanger(ABC):
    @abstractmethod
    def NotifyChange(self):
        pass