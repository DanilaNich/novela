import time
hpm = 100
def hp_maniken(hp):
    return hpm - attack
def Srajenie():
    print("Вы выбрали сражаться")
    time.sleep(2)
    print("Вы попытались атаковать этого монстра, но его кожа слишком тослстая и прочная что бы нанести урон")
    time.sleep(3)
    print("Гоблин-гигант раздовил вас")
    time.sleep(2)
    print("| Ваше приключение окончено |")
def trotil():
    print("Вы почему-то вместо того что-бы лечь спать подумали:")
    time.sleep(2)
    print("Хм а почему бы мне не посидеть на динамите ведь это так безопасно")
    time.sleep(3)
    print("Ну, исход очивиден, вы взорвались!")
def vipit_roma():
    print("вы выпили ром и опьянели")
    time.sleep(2)
    print("вместе с этим вам пришла в голову идея залезть на крышу и осмотреться")
    time.sleep(2)
    print("Вы не ударжались на лестнице и разбились")

while True:
    print("Добро пожаловать в игру")
    time.sleep(2)
    print("'Рыцарь из Лареона'")
    time.sleep(1)
    name = input("введите имя вашего героя: ")
    time.sleep(1)
    print("какое доблестное имя! Оно точно войдёт в историю")
    time.sleep(1)
    while True:
        try:
            age = int(input("какой возраст вашего героя? "))
            break
        except ValueError:
            print("Введите число")
    weapon_choice =input("выберите какое оружие будет у вашего рыцаря: 1 - меч, 2 - палка, 3 - десятитонный молот. ")
    if weapon_choice == "1":
        weapon = "меч";
    elif weapon_choice == "2":
        weapon = "палка"
    elif weapon_choice == "3":
        print("Вы попытались поднять молот но не смогли поэтому взяли лежавший рядом с ним нож")
        weapon = "Нож"
    else:
        print("Введите корректное число")

    knight_info = {
        "имя": name,
        "возраст": age,
        "оружие": weapon,
        "приключения": [],}
    def написать_информацию(рыцарь):
        return f"Имя: {рыцарь['имя']}\nВозраст: {рыцарь['возраст']} лет\nОружие: {рыцарь['оружие']}"
    time.sleep(2)
    print("Приключения начинаются!")
    time.sleep(2)
    if age > 80:
        print("Ваш герой был слишком стар и умер от сердечного приступа")
        time.sleep(2)
        print("| Ваше приключение окончено |")
        break
    elif age < 1:
        print("Ваш герой не родился")
        time.sleep(1)
        print("| Приключение окончено |")
        break
    elif age < 16:
        print("Ваш герой недостаточно опытен чтобы отправиться в приключение")
        time.sleep(2)
        print("| Ваше приключение окончено |")
        break

    print("В далёкие времена существовало княжество Лареон")
    time.sleep(4)
    print("Им правил  мудрый и добрый король по имени \033[32m\033Магнус")
    time.sleep(4)
    print("\033[0m Но вдруг на королевство напала армия Орков, так называемая \033[31m\033'Орда'")
    time.sleep(4)
    print("\033[0m Все воины ринулись в атаку, но нескончаемое количество орков давало о себе знать")
    time.sleep(4)
    print("Вскоре \033[31m\033Орда \033[0mсмогла пройти сквозь первые ряды оброны")
    time.sleep(4)
    print("И тогда Король решил обратиться к старцу за помощью")
    time.sleep(4)
    print("Старец посмотрел в свой шар пророка и сказал что скоро на свет появится Герой по имени", name)
    time.sleep(4)
    print("Который сможет одним ударом рассекать горы и врагов")
    time.sleep(4)
    print("Но до этого момента надо ещё продержаться 5 лет")
    time.sleep(4)
    print("Эта история про одного рыцаря")
    time.sleep(4)
    print(написать_информацию(knight_info))
    time.sleep(4)
    print("и вот ваш путь начался")
    time.sleep(2)
    print("Вам надо тренероваться чтобы стать сильнее")
    time.sleep(2)
    print("А вот и идёт ваш \033[32m\033 тренер \033[0m!")
    time.sleep(2)

    if weapon == "меч":
        print("\033[32m\033Тренер:\033[0m О! Я вижу ты выбрал хорошее оружие")
        time.sleep(2)
    elif weapon == "палка":
        print("\033[32m\033Тренер:\033[0m Что?! Какой глупец мог выбрать ПАЛКУ в качестве оружия???")
        time.sleep(2)
        print("\033[32m\033Тренер:\033[0m Вот держи булаву, будешь сражаться с ней")
        weapon = "Булава"
    elif weapon == "Нож":
        print("\033[32m\033Тренер:\033[0m Вижу ты любишь драться впритык к врагу")
        time.sleep(2)
        print("\033[32m\033Тренер:\033[0m почему такой выбор?")
        time.sleep(2)
        print("\033[32m\033Тренер:\033[0m Любишь смотреть в глаза Оркам когда вознаешь в них лезвие?")
        time.sleep(2)
        print("\033[32m\033Тренер:\033[0m А впрочем ниважно, на тренеровках это никак не скажется")
        time.sleep(2)
    print("\033[32m\033Тренер:\033[0m Выглядишь ты вполне неплохо, поэтому сразу начнём с тренировки")
    time.sleep(2)
    print("\033[32m\033Тренер:\033[0m Иди побей этот манекен, он не кусается, покажи что ты можешь")
    time.sleep(2)
    while True:
        print("перед вами стоит манекен")
        time.sleep(2)
        print("Здоровье манекена:", hpm)
        time.sleep(2)
        print("как бы вы хотели его ударить?")
        print("1 - Легонько")
        time.sleep(0.25)
        print("2 - сильно")
        while True:
            attack = input("Выбор:")
            if attack == "1":
                print("Вы подумали: 'доверя но проверяй!' и пэтому аккуратно тыкнули маникен своим оружием")
                time.sleep(2)
                print("кажется тренер сказал парвду, манекен не кусается")
                time.sleep(2)
                print("\033[32m\033Тренер:\033[0m Ну кто так бьёт то а?!")
                time.sleep(2)
                print("\033[32m\033Тренер:\033[0m Замахиваешся и бьёш что сложного? Ладно попробуй ещё раз")
                time.sleep(2)
                print("Как вы хотите ударить маникен?")
                time.sleep(2)
                print("1 - Легонько")
                time.sleep(0.25)
                print("2 - сильно")
                attack = input("Выбор:")
                if attack == "1":
                    print(
                        "\033[32m\033Тренер\033[0m сказал вам ударить сильно но у вас появилось неприодолимое желание тыкнуть маникен ещё раз")
                    time.sleep(4)
                    print("Вы это и сделали, вы тыкнули маникен своим оружием")
                    time.sleep(2)
                    print("кажется \033[32m\033Тренер\033[0m пришёл в ярость")
                    time.sleep(2)
                    print("Он набросился на манекен со словами:'ВОТ ТАК НАДО БИТЬ!!!")
                    time.sleep(2)
                    print("Он избивал манекен пока из него не пошла вата")
                    time.sleep(1)
                    print("\033[32m\033Тренер:\033[0mЛадно думаю урок усвоен, можешь идти отдыхать")
                    break
                    time.sleep(2)
                elif attack == "2":
                    attack = 50
                    print("Здоровье манекена:", hp_maniken(hpm))
            elif attack == "2":
                attack = 50
                print("Здоровье манекена:", hp_maniken(hpm))
                print("\033[32m\033Тренер:\033[0mМолодец! Очень хороший удар, от него манекен чуть не развалился")
                time.sleep(2)
                print("\033[32m\033Тренер:\033[0mА теперь покажи свой добивающий удар!")
                time.sleep(2)
                while True:
                    dobivanie_manike = input("введите 1 что бы совершить добивающий удар")
                    if dobivanie_manike == "1":
                        attack = 100
                        print("Здоровье маникена:", hp_maniken(hpm))
                        time.sleep(2)
                        print("\033[32m\033Тренер:\033[0mМолодец! Можешь отдыхать")
                        break
                    else:
                        print(
                            "я не придумал что тут написать поэтому давайте вы просто в следующий раз введёте '1' и мы сделаем вид что этого диалога не было")
                        time.sleep(2)
                break
            else:
                print("выберите корректное действие")
        print("Вы отправились в свою комнату чтобы отдохнуть")
        time.sleep(2)
        break
    print("В комнате находились: пустой шкаф, кровать, динамит и бутылка рома")
    time.sleep(2)
    print("что бы хотели сейчас сделать?")
    time.sleep(1)
    print("1 - выпить рома")
    time.sleep(1)
    print("2 - посидеть на динамите")
    time.sleep(1)
    print("3 - лечь спать")
    while True:
        room_choice = input("вы хотели бы: ")
        if room_choice == "1":
            print(vipit_roma())
            time.sleep(2)
            print("Благо это был лишь сон и")
            break
        elif room_choice == "2":
            print(trotil())
            time.sleep(2)
            print("благо это был лишь сон и")
            break
        elif room_choice == "3":
            print("вы легли спать")
            time.sleep(2)
            break
    print("Вы проснулись из-за того что услышали гул дозорных труб")
    time.sleep(3)
    print("Вы выбежали из здания и спросили у пробегавшего мимо солдата что происходит")
    time.sleep(3)
    print("Он лишь прокричал: 'Они идут!'")
    time.sleep(2)
    print("Вы посмотрели вперёд и увиденное шокировало вас")
    time.sleep(2)
    print("\033[31m\033'Орда'\033[0m надвигалась на город в котором вы находились")
    time.sleep(4)
    print("Вдруг вы услышали какой-то грохот и обернулись")
    time.sleep(2)
    print("Прямо позади вас стоял гоблин колоссальных размеров!")
    time.sleep(3)
    print("душа говорила сражаться, а здравый смысл бежать!")
    time.sleep(2)
    print("но что выберите вы?")
    time.sleep(2)
    while True:
        print("1 - сражаться")
        Koncovka = input("2 - бежать")
        if Koncovka == "1":
            print(Srajenie())
            break
        if Koncovka == "2":
            print("Вы попытались убежать от Гоблина-гиганта")
            time.sleep(2)
            print("Но он кинул в вас дубинку и раздовил")
            time.sleep(2)
            print("| Ваше приключение окончено |")
            time.sleep(2)
            print("Да, героем, который спасёт это королевство от нашествия, которого звали", name)
            time.sleep(2)
            print("Были не вы")
            break
    break