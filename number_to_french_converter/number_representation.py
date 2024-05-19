from dataclasses import dataclass, field
from typing import Optional, Protocol, List, Dict

from .constants import UNITS, MILLIONS


class NumberRepresentation(Protocol):
    def to_text(self) -> str: ...


@dataclass
class LessThanAThousand:
    decades_str_dict: Dict[int, str]

    val: int

    unit: int
    decades: List[int]
    hundred: Optional[int] = field(default=None)

    @staticmethod
    def decades_and_unit_connecter(decades: List[int], unit: int) -> str:
        decade = sum(decades)
        return "-et-" if unit in [1, 11] and decade != 80 else "-"

    def to_text(self) -> str:
        hundred_and_decades = []

        if self.hundred is not None:
            if self.hundred > 1:
                hundred_and_decades.append(UNITS[self.hundred])
            hundred_and_decades.append("cent")
        hundred_and_decades.extend(map(self.decades_str_dict.get, self.decades))

        if len(hundred_and_decades) == 0:
            return UNITS[self.unit]
        else:
            hundred_and_decades_str = "-".join(hundred_and_decades)
            if self.unit == 0:
                return hundred_and_decades_str
            else:
                return (
                    hundred_and_decades_str
                    + self.decades_and_unit_connecter(
                        decades=self.decades, unit=self.unit
                    )
                    + UNITS[self.unit]
                )


@dataclass
class MoreThanAThousand:
    val: int
    list_hundreds: list[LessThanAThousand]

    def to_text(self) -> str:
        list_hundreds_str = []
        for rank, elem in enumerate(self.list_hundreds):
            if elem == 0:
                continue
            else:
                if rank > 0:
                    list_hundreds_str.append(MILLIONS[rank])
                if elem.val > 1:
                    list_hundreds_str.append(elem.to_text())
        return "-".join(reversed(list_hundreds_str))
