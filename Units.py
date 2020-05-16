from abc import ABCMeta, ABC, abstractmethod

COST_OF_UNIT_HUMAN = 10
COST_OF_UNIT_CLIRICK = 15
class Unit(metaclass=ABCMeta):
    """
    Абстрактный компонент, в данном случае это - отряд (отряд может
    состоять из одного солдата или более)
    """
    atack = 30

    @abstractmethod
    def print(self) -> None:
        """
        Вывод данных о компоненте
        """
        pass

class Human(Unit):
    atack = 30
    def print(self) -> None:
        print('Человек', end=' ')

class Clirick(Unit):
    atack = 40
    def print(self) -> None:
        print('Клирик', end=' ')



class ArmyFactory(ABC):
    """
    абстрактная фабрика
    """
    @abstractmethod
    def create(self):
        pass


class CorfagenArmyFactory(ArmyFactory):

    def create(self, race="human"):
        if race == "human":
            return self.Human()
        elif race == "clirick":
            return self.Clirick()


class SerbianArmyFactory(ArmyFactory):

    def create(self, race="human"):
       if race == "human":
            return self.Human()
       elif race == "clirick":
            return self.Clirick()

class Squad(Unit):
    money = 100

    def __init__(self, name_of_troop):
        self._units = []
        self.name = name_of_troop
        self.atack = 0

    def print(self) -> None:
        for u in self._units:
            if type(u) is Squad:
                print("Армия {} (".format(self.name), end=' ')
                break
        else:
            print("Отряд {} (".format(self.name), end=' ')
        for u in self._units:
            u.print()
        print(')')

    def func(self, unit: Unit):
        self._units.append(unit)
        self.atack += unit.atack
        unit.print()
        print('присоединился к отряду {}'.format(self.name))
        print()

    def add(self, unit: Unit) -> int:
        """
        Добавление нового отряда

        :param unit: отряд (может быть как базовым, так и компоновщиком)
        """
        if type(unit) is Clirick:
            if self.money >= COST_OF_UNIT_CLIRICK:
                self.func(unit)
                self.money -= COST_OF_UNIT_CLIRICK
            else:
                print("Не хватает средств")
        elif type(unit) is Human:
            if self.money >= COST_OF_UNIT_HUMAN:
                self.func(unit)
                self.money -= COST_OF_UNIT_HUMAN
            else:
                print("Не хватает средств")
        elif type(unit) is Squad:
            self.func(unit)
        else:
            print("TROBBLES")
            return
        return self.money


    def remove(self, unit: Unit) -> None:
        """
        Удаление отряда из текущего компоновщика

        :param unit: объект отряда
        """
        print(unit)
        for u in self._units:
            if u == unit:
                self._units.remove(u)
                u.print()
                print('покинул отряд {}'.format(self.name))
                print()
                break
        else:
            unit.print()
            print('в отряде {} не найден'.format(self.name))
            print()

    def delete(self):
        del self._units
