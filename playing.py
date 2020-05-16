import Units

names = {}
GOAL = 500
REZ = 20

def usage():
    phr = "Будь внимателен, в этой игре используется ангийская раскладка!\n"
    phr += "Ты можешь нанимать специальных воинов клириков для сражений, каждый воин стоит 15 монет. \n"
    phr += "Кроме того ты можешь нанимать обычных людей, они стоят дешевле, "
    phr += "но знай боевая мощь клириков сильнее!\n"
    phr += "Чтобы объеденить отряд и создать армию введи 'g' далее 'enter'.\n"
    phr += "Чтобы вступить в бой введи клавишу 's' далее 'enter'\n"
    phr += "Чтобы создать новый отряд войска введи 'd' и 'enter'\n"
    phr += "Чтобы вызвать usage, введи 'f' далее 'enter'\n"
    phr += "Чтобы узнать боевую мощь войска введи 'i' далее 'enter'\n"
    phr += "Чтобы добавить в войско нового воина введи 'a' далее 'enter'\n"
    phr += "Чтобы завершить игру, введи любую другую клавишу"
    phr += "Чтобы узнать состав войска введи 'k' далее 'enter'"
    print(phr)

def atack(a1: str, army1: Units.Squad, a2: str, army2: Units.Squad) -> int:
    if army1.atack > army2.atack:
        print("Победила армия {}! Она получает 20 золотых!\n".format(a1))
        army1.money += REZ
        if army1.money >= GOAL:
            print("Власть в государстве у армии {}! ".format(a1))
            print("Игра окончена...")
            return
    elif army2.atack > army1.atack:
        print("Победила армия {}! Она получает 20 золотых!\n".format(a2))
        army2.money += REZ
        if army2.money >= GOAL:
            print("Власть в государстве у армии {}! ".format(a2))
            print("Игра окончена...")
            return
    else:
        print("Ничья!")


def play(player):
    money = 70
    print("Пора начинать собирать армию, давай создадим отряд!")
    name = input("Назови свой отряд: ")
    squad = name
    squad = Units.Squad(name)#создали отряд с именем нейм
    names[name] = squad
    print("Мы добавим в него двух людей\n")
    for i in range(2):
        squad.add(Units.Human())
    print("Итак, твой отряд состоит из 2 человек. ")
    print("Боевая мощь отряда равна {} ".format(squad.atack))
    usage()
    while 1:
        character = input()
        if character == "a":
            race = input("Введи рассу: clirick или human: ")
            name = input("Введи название своей армии или отряда: ")
            if name in names:
                if race == "clirick":
                    names[name].money = names[name].add(Units.Clirick())
                    print("Боевая мощь этого войска равна {} ".format(squad.atack))
                elif race == "human":
                    names[name].money = names[name].add(Units.Human())
                    print("Боевая мощь этого войска равна {} ".format(squad.atack))
                else:
                    print("Расса введена неправильно, попробуй еще раз!")
                    continue
                print("У войска осталось {} монет".format(names[name].money))
            else:
                print("Введено несуществующее название войска или рассы, попробуй еще раз!")
                continue
        elif character == "s":
            first = input("Введи 1ое войско: ")
            second = input("Введи 2ое войско: ")
            if first and second in names:
                for u in names[second]._units:
                    if u == names[first]:
                        print("{} войско содержит {} войско".format(second, first))
                        break
                else:
                    for u in names[first]._units:
                        if u == names[second]:
                            print("{} войско содержит {}".format(first, second))
                            break
                    else:
                        atack(first, names[first], second, names[second])
                print("Помни, войска не должны пересекаться!")
                continue
            else:
                print("Введены несуществующие войска! Попробуйте заново\n")
        elif character == "d":
            name = input("Назови свой отряд: ")
            squad = name
            squad = Units.Squad(name)
            names[name] = squad
            print("Теперь нужно добавить воинов, для этого используй клавишу 'a' и 'enter'\n")
            print("Не забудь вписать название отряда, который ты только что создал.\n")
        elif character == "f":
            usage()
        elif character == "g":
            first = input("Введи 1ое войско: ")
            second = input("Введи 2ое войско: ")
            if first in names:
                if second in names:
                    for u in names[second]._units:
                        if u == names[first]:
                            print("{} войско содержит {} войско".format(second, first))
                            break
                    else:
                        for u in names[first]._units:
                            if u == names[second]:
                                print("{} войско содержит {}".format(first, second))
                                break
                        else:
                             names[second].add(names[first])
                             del names[first]
                             print(names)
                             print("Боевая мощь этого войска равна {} ".format(names[second].atack))
                else:
                    print("Введено несуществующее название")
            else:
                print("Введено несуществующее название")
        elif character == "i":
             str = input("Введи название отряда: ")
             if str in names:
                 print(names[str].atack)
        elif character == "k":
            troop_number = input("Введи название войска, чей состав хочешь знать: ")
            if troop_number in names:
                    names[troop_number].print()
        else:
            choise = input("Вы хотите выйти из игры? Введите 'да', для подтверждения: ")
            if choise == "да":
                return
            else:
                print("Отлично, продолжаем!")
                continue







