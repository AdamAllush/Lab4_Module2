class KettlebellСollection:
    def __init__(self, kettlebell_number: int, kettlebell_price: float):
        """
        Создание и подготовка к работе объекта "Коллекция шаров для боулинга"
        :param kettlebell_number: Колличество шаров для боулинга в коллекции
        :param kettlebell_price: Стоимость всех шаров для боулинга
         Примеры:
        >>> kettlebell = KettlebellСollection(999, 189000)  # инициализация экземпляра класса
        """
        if not isinstance(kettlebell_number, int):
            raise TypeError("Число шаров для боулинга в коллекции должно быть типа int")
        if kettlebell_number < 0:
            raise ValueError("Число шаров для боулинга в коллекции должно быть положительным числом")
        self.kettlebell_number = kettlebell_number
        if not isinstance(kettlebell_price, (int, float)):
            raise TypeError("Цена шаров для боулинга в коллекции должна быть типа int или float")
        if kettlebell_price < 0:
            raise ValueError("Цена шаров для боулинга в коллекции должна быть положительным числом")
        self.kettlebell_price = kettlebell_price


    def __str__(self):
        """ Метод str, возвращающий колличество и стоимость шаров для боулинга в коллекции"""
        return f"Колличество шаров для боулинга {self.kettlebell_number}. Стоимость коллекции {self.kettlebell_price}."


    def __repr__(self):
        """ Метод repr, возвращающий колличество и стоимость шаров для боулинга в коллекции"""
        return f"{self.__class__.__name__}(kettlebell_number={self.kettlebell_number!r}, kettlebell_price={self.kettlebell_price!r})"


    def single_kettlebell(self) -> float:
        """
        Функция которая определяет цену одного шара
        :return: Цена одного шара
        Примеры:
        >>> kettlebell  = KettlebellСollection(999, 18900.0)
        >>> kettlebell.single_kettlebell()
        """
        ...
    def coolest_kettlebell(self) -> int:
        """
            Функция, которая определяет самый лучший шар для боулинга
            :return: Случайный номер шара из общего числа шаров для боулинга
            Примеры:
            >>> kettlebell  = KettlebellСollection(999, 18900.0)
            >>> kettlebell.coolest_kettlebell()
            """
        ...

class Kettlebell(KettlebellСollection):
    def __init__(self, kettlebell_number: int, kettlebell_price: float, kettlebell_weight: float):
        """
        Создание и подготовка к работе объекта "Коллекция шаров для боулинга"
        :param kettlebell_number: Колличество шаров в коллекции
        :param kettlebell_price: Стоимость всех шаров для боулинга
        :param kettlebell_weight: Масса шара для боулинга
         Примеры: kettlebell  = Kettlebell(999, 18900.0,9.5)
         """
        if not isinstance(kettlebell_weight, (int, float)):
            raise TypeError("Масса шара должна быть типа int или float")
        if kettlebell_weight < 0:
            raise ValueError("Масса шара должна быть положительным числом больше нуля")
        self.kettlebell_weight = kettlebell_weight

    def __repr__(self):
        """ Метод repr, возвращающий колличество и стоимость шаров в коллекции, вес заданного шара"""
        return f"{self.__class__.__name__}(kettlebell_number={self.kettlebell_number!r}, kettlebell_price={self.kettlebell_price!r}, kettlebell_weight={self.kettlebell_weight!r} )"
    def coolest_kettlebell(self) -> int:
        """
            Функция, которая определяет самый лучший шар для боулинга
            :return: Выводит заданный вес шара для боулинга, определяя текущий шар как самый лучший
            Примеры:
            >>> kettlebell  = Kettlebell(999, 18900.0, 500)
            >>> kettlebell.coolest_kettlebell()
            """
        ...

if __name__ == "__main__":
    pass