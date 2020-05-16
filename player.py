import Units
import playing


phr = "После смерти короля в нашей стране происходят междоусобицы и войны!\n"
phr += "Только ты можешь нам помочь, разреши войну, выяви победителя!"

def func():
    player = input("Please, choose and enter your username: ")
    print("Привет, " + player + "!")
    i = 0
    while True:
        i += 1
        try:
            race = input("Выбери страну, в которой хочешь играть: Carfagen, Serb ")
            if race.lower() == "carfagen":
                player = Units.CorfagenArmyFactory()
                print("Поздравляю! Твой стартовый капитал 100 монет\n")
                print(phr)
                break
            elif race.lower() == "serb":
                player = Units.SerbianArmyFactory()
                print("Поздравляю! Твой стартовый капитал 100 монет\n")
                print(phr)
                break
            else:
                print("Unknown race!")
                raise ValueError
        except ValueError:
            if i < 2:
                print("Choose again.")
            elif i == 2:
                print("Too many times entered wrong line, bye-bye baby)")
                print("I'm just joke, choose one more time!")
            else:
                 return
            continue
    print()
    playing.play(player)

#Вызов функции
func()