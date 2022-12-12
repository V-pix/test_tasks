from dataclasses import dataclass


@dataclass(frozen=True)
class Technic:
    expensive_price: int = 1000000
    budgetary: str = "Бюджетный"
    expensive: str = "Дорогой"

    def __init__(self, name: str, price: int, availability: bool) -> None:
        self.name = name
        self.price = price
        self.availability = availability

    def __lt__(self, other: "Technic"):
        len_self = len(self.name)
        len_other = len(other.name)
        return len_self < len_other

    def price_of_product(self):
        print(
            Technic.budgetary
            if self.price < Technic.expensive_price
            else Technic.expensive
        )


if __name__ == "__main__":
    a = Technic("product 123123", 150000, True)
    a.price_of_product()
    b = Technic("product 253", 15000, True)
    print(a > b)
