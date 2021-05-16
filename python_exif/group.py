from dataclasses import dataclass
from typing import Optional


@dataclass
class Group:
    min: Optional[int]
    max: Optional[int]
    count: int

    def incr(self):
        self.count += 1

    def has(self, value: int) -> bool:
        return (self.min is None or self.min < value) and \
               (self.max is None or value <= self.max)

    def name(self) -> str:
        return f'{self.min or ""}-{self.max or ""}'
