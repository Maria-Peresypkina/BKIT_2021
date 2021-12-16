from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):

    @property  # property позволяет превратить метод класса в атрибут класса

    @abstractmethod  # Абстрактным называется объявленный, но не реализованный метод
    def product(self) -> None:
        pass

    @abstractmethod  # Абстрактным называется объявленный, но не реализованный метод
    def tshirt(self) -> None:  # футболка
        pass

    @abstractmethod
    def pullover(self) -> None:  # свитер
        pass

    @abstractmethod
    def jeans(self) -> None:  # джинсы
        pass


class Clothes_Builder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Shop()

    @property  # property позволяет превратить метод класса в атрибут класса
    def product(self) -> Shop:
        product = self._product
        self.reset()
        return product

    def tshirt(self) -> None:
        self._product.add("футболка")

    def pullover(self) -> None:
        self._product.add("свитер")

    def jeans(self) -> None:
        self._product.add("джинсы")


class Shop():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"В магазине продаются: {', '.join(self.parts)}", end="")


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property  # property позволяет превратить метод класса в атрибут класса
    def builder(self) -> Builder:
        return self._builder

    @builder.setter  # применяется сеттер к методу builder, то есть делаем метод доступным для записи
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def HM(self) -> None:
        self.builder.pullover()
        self.builder.tshirt()

    def Bershka(self) -> None:
        self.builder.jeans()
        self.builder.pullover()


if __name__ == "__main__":
    director = Director()
    builder = Clothes_Builder()
    director.builder = builder

    print("HM: ")
    director.HM()
    builder.product.list_parts()

    print("\n\nBershka: ")
    director.Bershka()
    builder.product.list_parts()