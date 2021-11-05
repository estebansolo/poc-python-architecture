from typing import Iterable

from pydantic import BaseModel

from source.shared.domain.hardcuts.models.hardcuts import AgeHardcut


class Hardcuts(BaseModel):
    age_hardcut: AgeHardcut

    def __iter__(self) -> Iterable[Hardcut]:
        return (
            getattr(self, hardcut)
            for hardcut in self.__fields__.keys()
            if getattr(self, hardcut) is not None
        )