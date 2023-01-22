from dataclasses import dataclass


@dataclass()
class Math:
    a: int
    b: int

    def __add__(self, other) -> object:
        return Math(self.a + other.a, self.b + other.b)

    def raise_power(self) -> int | float:
        return self.a ** self.b


def main():
    math = Math(2, 6.5)
    print(math.raise_power())
    print(math.a + math.b)
    print(math + math)


if __name__ == '__main__':
    main()
