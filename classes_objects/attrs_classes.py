import attr
from datetime import date


@attr.s
class Employee:
    id: int = attr.ib(converter=int)
    first_name: str = attr.ib(converter=str)
    middle_initial: str = attr.ib(converter=str)
    last_name: str = attr.ib(converter=str)
    age: int = attr.ib(converter=int)


