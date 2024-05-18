from dataclasses import dataclass, field
from typing import Optional

from .constants import DECADES, UNITS, MILLIONS


@dataclass
class LessThanAHundred:
    val: int

    _unit: int = field(init=False)
    _decade: Optional[int] = field(default=None, init=False)

    def __post_init__(self):
        if self.val < 20:
            self._unit = self.val
        else:
            self._unit = self.val % 10
            self._decade = self.val - self._unit
            if self._decade == 70 or self._decade == 90:
                self._decade -= 10
                self._unit += 10

    def to_text(self) -> str:
        if self._decade is None:
            return UNITS[self._unit]
        else:
            if self._unit == 0:
                return DECADES[self._decade]
            connecter = (
                "-et-"
                if (self._unit == 1 or self._unit == 11) and self._decade != 80
                else "-"
            )
            return f"{DECADES[self._decade]}{connecter}{UNITS[self._unit]}"


@dataclass
class LessThanAThousand:
    val: int

    _unit: int = field(init=False)
    _hundred: Optional[int] = field(default=None, init=False)

    def __post_init__(self):
        self._unit = self.val % 100
        if self._unit < self.val:
            self._hundred = self.val // 100

    def to_text(self) -> str:
        unit = LessThanAHundred(self._unit)
        if self._hundred is None:
            return unit.to_text()
        else:
            hundred_str = (
                "cent" if self._hundred == 1 else f"{UNITS[self._hundred]}-cent"
            )
            return hundred_str if unit.val == 0 else f"{hundred_str}-{unit.to_text()}"


@dataclass
class MoreThanAThousand:
    pass
