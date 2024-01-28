import time
from datetime import datetime
current_datetime = datetime.now()
print(current_datetime)
def privetstvie():
    print("Добро пожаловать в игру:")
    time.sleep(1)
    print("'52 аномилиb'")
    time.sleep(1)
    print("Что бы узнать автора введите, во время вопроса про сохранение кодовое слово: 'Avtor'")
    time.sleep(1)
    print("Чит команда на быстрое прохождение, во время вопроса про сохранение кодовое слово: 'Fast'")
steps = {
    1: {print (privetstvie())},
    1: {"Text": "Вы оказались по среди пустой комнаты и не помните что произошло."
                "Осмотревшись вы видите единственную дверь."
            "Хотели бы вы её открыть?", "Yes": 2, "No": 3},
    2: {"Text": "Вы открыли дверь и увидели лес. "
                "Вам ужасно хотелось пить и вы увидели лимонный гараж."
            "Хотитет попить его?", "Yes": 4, "No": 5},
    3: {"Text": "Вы остались в комнате и умерли от обезвоживания."
                "\033[31m\033Плохая концовка №1\033[0m",
            "Игра окончена": True},
    4: {"Text": "Вы решили выпить гаражик и уталили жажду. "
                "Неподалёку была тропинка ведущая в питер, а также рядом стоял сундук. "
            "Хотите заглянуть в сундук?", "Yes": 9, "No":8},
    5: {"Text": "Вы не захотели пить гаражик поэтому осмотрелись по сторонам и нашли сундук, в нём лежала банка адреналина. "
            "Хотите ли её выпить?", "Yes": 7, "No":6},
    6: {"Text": "Вы не захотели пить адреналин, но в округе больше не было воды и поэтому вы умерли от обезвоживания. "
                "\033[31m\033Плохая концовка №2\033[0m",
            "Игра окончена": True },
    7: {"Text": "Вы выпили энергос, которая лежал в сундуке, и решили осмотреться. "
                "Рядом с вами была дорога ведущая в питер. "
            "Хотите пойти по ней?", "Yes":10, "No":11},
    8: {"Text": "Вы не захотели посмотреть что лежит в сундуке и недолго думав решили пойти по тропе из-за того что больше делать нечего. "
            "Введите Y или N для продолжения", "Yes":10, "No":10},
    9: {"Text": "Вы заглянули в сундук и увидели адреналин, но поскольку вы уже утоили жажду, оставили энергос в сундуке."
                "Делать здесь было больше нечего поэтому вы решили пойти по тропе. "
            "Введите Y или N для продолжения", "Yes":10, "No":10},
    10: {"Text": "Вы пошли в питер и встали посреди палящего солнца, но увидели под своими ногами люк. "
                 "Хотите ли вы его открыть?", "Yes": 26,"No":11},
    11: {"Text": "Как бы вам не было интересно что находится под этим люком вы решили не открывать его."
                 " Вы решили пойти дальше по тропе через питер. "
            "Введите Y или N для продолжения", "Yes":12, "No":12},
    12: {"Text": "Вы шли по тропинке и пришли к её ответвлению. "
            "Хотите свернуть?", "Yes": 13, "No":16},
    13: {"Text": "Вы захотели посмотреть куда ведёт ответвление дороги и пришли к обрыву с которого открывается хороший вид на финляндию. "
            "Хотите ли спрыгнуть с него?", "Yes": 14, "No":15},
    14: {"Text": "Подумав что прыгнуть с обрыва будет довольно весело вы это и сделали, но ничего весёлого не произошло, вы просто разбились. "
                 "\033[31m\033Плохая концовка №3\033[0m",
            "Игра окончена": True},
    15: {"Text": "Хорошо подумав вы не стали прыгать и пошли по тропинке в обратную сторону. "
            "Введите Y или N для продолжения", "Yes":12, "No":12},
    16: {"Text": "Вы не захотели сворачивать и пошли дальше по дороге, которая привела вас к старой избе, из которой исходили странные звуки. "
            "Хотели бы вы зайти в неё?", "Yes":17, "No":19},
    17: {"Text": "Вы зашли в избу и увидели наливкина. "
                 "Он выстрелил из рпг и вы потеряли сознание."
            "Введите Y или N для продолжения", "Yes":18, "No":18},
    18: {"Text": "Вы очнулись в тюрьме. "
                 "Там вы и провели остатки своей жизни. "
                 "\033[31m\033Плохая концовка №4\033[0m",
            "Игра окончена": True},
    19: {"Text": "Вы решили не заходить в избу, как из нее вышел наливкин и побежал на вас. "
            "Что вы хотите делать? Y - драться, N - бежать", "Yes":20, "No":21},
    20: {"Text": "Вы со всей силы влетели в него с ноги и упали, он на удивление оказалась сильнее чем вы думали. "
                 "Он с одного удара положил вас в нокаут. "
            "Введите Y или N для продолжения", "Yes":18, "No":18},
    21: {"Text": "Вы решили спасаться бегством и побежали в поле. "
            "Введите Y или N для продолжения", "Yes":22, "No":22},
    22: {"Text": "Прибежав в поле вы увидели группу военных которые стояли в боевой готовности, один из них закричал:'Беги к нам быстрее!'. "
            "Что вы сделаете? Y - побежать к военным N - стоять на месте", "Yes":23, "No":24},
    23: {"Text": "Вы стояли на месте смотря с сомнением смотря на военных и наливкин взорвал  вас. "
                 "\033[31m\033Плохая концовка №4\033[0m",
            "Игра окончена": True},
    24: {"Text": "Вы побежали к военным и едва добежа до них из леса показался наливкин, Огонь!"
                 "прокричал один из военных и открыл огонь, спустя пару пуль наливкин был застрелена. "
            "Введите Y или N для продолжения", "Yes":25, "No":25},
    25: {"Text": "Один из военных обратился к вам 'Не бойся мы специальная военная группа по борьбе с аномалиями под кодовым названием '52'. "
                 "Лучше иди в бункер, там безопаснее, а мы пока что избавимся от депутата. "
            "Введите Y или N для продолжения", "Yes":26, "No":26},
    26: {"Text": "Вы спустились в бункер и увидели целую базу военных. "
            "Введите Y или N для продолжения", "Yes":27, "No":27},
    27: {"Text": "К вам подошёл военный и сказал 'Приветствую тебя на военной базе '52'."
            "провести экскурсию?", "Yes":29, "No":28},
    28: {"Text": "Вы отказались от экскурсии и решили сами всё осмотреть. "
                 "Перед вами был выбор осмотреть помещения или ознакомиться с документацией. "
            "Хотели бы вы осмотреть помещения и пропустить документацию?", "Yes":33, "No":29},
    29: {"Text": "Вы решили ознакомиться с докуминтацией по объектам '52'."
                 "В ней была информацию по трём объектам"
            "Введите Y или N для продолжения", "Yes":30, "No": 30},
    30: {"Text": "Первым был объект под номером 'SCP - 352'."
         "Имя объекта - наливкин."
                 "Дополнительные сведения: "
                 "SCP-352 представляет собой очень старого, истощенного мужика неопределенного возраста и расы. "
                 "SCP-352 говорит на старославянском языке."
                 "Хотите изучить следующий объект?",
         "Yes":31, "No":33},
    31: {"Text": "Второй объект был под номером 'SCP-096'."
         "Имя объекта - Скромник"
         "Дополнительные сведения:"
         "SCP-096 – гуманоидное существо ростом приблизительно 2,38 метра. "
         "У субъекта наблюдается малое количество мышечной массы, предварительные анализы массы тела показывают легкое недоедание."
         "Хотите изучить последний объект?",
         "Yes":32, "No":33},
    32: {"Text": "Третий объект был под номером 'SCP-019'."
         "Имя объекта 'Чудовищная ваза'."
         "Дополнительные сведения:"
         "SCP-019 - это очень большая керамическая ваза высотой 2.4 м, диаметр горлышка равен 1.8 м. "
         "Стиль и декор указывают на то, что она была создана в Классической Греции. "
         "Но установление точного возраста невозможно ввиду полной неуязвимости объекта к любым видам повреждений."
         "Вы прочитали всю необходимую документацию по объектам фонда."
         "Введите Y или N для продолжения",
         "Yes":33, "No":33},
    33: {"Text": "Вы начали осматривать бункер."
                 "В самом его конце была большая дверь с жёлтой изолентой."
                 "Вы подошли поближе и прочли 'Вход строго запрещён!'."
                 "Хотите ли вы открыть дверь?",
         "Yes":34, "No":36},
    34: {"Text": "Вы открыли дверь и зашли внутрь комнаты."
                 "В самом её центре был портал с табличкой."
                 "На табличеке было написано 'Выход в реальность'"
                 "Хотите ли вы войти в портал?",
         "Yes":35, "No":37},
    35: {"Text": "Вы вошли в портал."
                 "Всё резко утихло и стало темно."
                 "Вы проснулись от звона будильника."
                 "Добро пожаловать в реальность!"
                 "\033[32m\033Хорошая концовка №1\033[0m",
         "Игра окончена": True},
    36: {"Text": "Вы не стали открывать дверь. Вдруг вы услышали вой сирен и увидели как неизвестное существо громило бункер. Оно растерзало вас."
                 "\033[31m\033Плохая концовка №5\033[0m",
         "Игра окончена": True},
    37: {"Text": "Вдруг сзади вас раздался голос. Ты уже знаешь слишком много. Вас убил повстанец хаоса.",
                 "\033[31m\033Плохая концовка №6\033[0m"
         "Игра окончена": True},
    100: {"Text": "Вы воспользовались читом быстрая концовка."
                  "Вы получили ачивку 'мухлёр'.\n"
                  "\033[31m\033САМАЯ Плохая концовка\033[0m",
          "Игра окончена": True},
    101: {"Text": "Автор: salava club."
                  "Тем не менее вы разбили четвёртую стену."
                  "Нейтральная концовка",
        "Игра окончена": True, },
}
def load_game_progress():
    while True:
        try:
            with open('game_progress.txt') as f:
                savechoice = input("Загрузить существующее сохранение? (Y/N) ")
                if savechoice == "Y":
                    return int(f.readlines()[0])
                elif savechoice == "y":
                    return int(f.readlines()[0])
                elif savechoice == "N":
                    print("Начало новой игры...")
                    with open('game_progress.txt', 'w') as f:
                        f.write(str(1))
                    return 1
                elif savechoice == "n":
                    print("Начало новой игры...")
                    with open('game_progress.txt', 'w') as f:
                        f.write(str(1))
                    return 1
                elif savechoice == "Fast":
                    return 100
                elif savechoice == "Avtor":
                    return 101
                else:
                    print("Неверный ввод, пожалуйста напишите 'Y' или 'N' и нажмите  Enter")
        except:
            print("Сохранение не найдено.")
            print(" Начало новой игры...")
            time.sleep(3)
            return 1

def process_answer(i):
    answer = input(steps[i]['Text'] + " (Y/N/Save) ")

    if answer.lower() == "y":
        return steps[i]['Yes']

    if answer.lower() == "Y":
        return steps[i]['Yes']

    if answer.lower() == "n":
        return steps[i]['No']

    if answer.lower() == "N":
        return steps[i]['No']

    if answer.lower() == "save":
        with open('game_progress.txt', 'w') as f:
            f.write(str(i))
            print("Игра сохранена. Возврат к повествованию:")
        return i
    if i == 1:
        with open('game_progress.txt', 'w') as f:
            f.write(str(i))

    print('\n⚠ Неверный ввод; пожалуйста напишите "Y", "N", или "SAVE" - и нажмите Enter.\n')
    return i


if __name__ == '__main__':
    index = load_game_progress()

    while not steps[index].get("Игра окончена", False):
        index = process_answer(index)

    print(steps[index]['Text'])
    with open("binary_progress", 'wb') as file:
        file.write(index, current_datetime)
    print("Поздравления! Вы прошли игру.")

def process_fastend(i):
    answer = input(steps[i]['Text'] + " (Y/N/Save) ")
    if answer.lower() == "Fast":
        return 100

def inforamt(i):
    answer = input(steps[i]['Text'] + " (Y/N/Save) ")
    if answer.lower() == "Avtor":
        return 101