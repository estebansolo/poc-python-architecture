from abc import abstractmethod
from typing import Optional

from pydantic import BaseModel


class Hardcut(BaseModel):
    is_active: bool
    passed: Optional[bool] = None
    bypass: Optional[bool] = None

    @abstractmethod
    def evaluate(self, data) -> None:
        raise NotImplementedError


class AgeHardcut(Hardcut):
    age_upper_bound: int
    age_lower_bound: int
    age_range: Optional[str] = None

    def evaluate(self, data) -> None:
        pass

    def __str__(self):
        return 'age_filter'
