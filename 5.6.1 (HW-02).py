pobeditel = 0 # Это переменная для уточнения какой игров победил и должны ходи продолжиться
varianti = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] # это список цифр из которого формируеться карта
igrok_1 = [] # список ходов игрока 1
igrok_2 = [] # список ходов игрока 2
win_nummbers = [['1', '2', '3'], # выигрышные комбинации, программа постоянно проверет, есть ли комбинация в списке игрока
                ['4', '5', '6'],
                ['7', '8', '9'],
                ['1', '4', '7'],
                ['2', '5', '8'],
                ['3', '6', '9'],
                ['1', '5', '9'],
                ['3', '5', '7']
                ]

def tabliza(x):
    """Эта функция выводит карту ходов и карту с ходами"""
    print(f"{x[6]} {x[7]} {x[8]}\n"
          f"{x[3]} {x[4]} {x[5]}\n"
          f"{x[0]} {x[1]} {x[2]}")


def fahler(x):
    """Эта функция проверяет ошибки ввода и на свободное место для хода"""
    while True:
        try:
            choice = int(input(f"{x} игрок. Выберите место (цифру): ")) - 1
            if choice < 0 or choice > 9:
                print("Не правильная цифра")
                continue
            elif varianti[choice] == 'o' or varianti[choice] == 'x':
                print("Место уже занято")
                continue
            else:
                return choice
        except:
            print("Ошибка ввода")
            continue


def summa(win_nummbers, choice):
    """Это функция проверяет список ходов игрока на наличие выигрышной комбинации"""
    for item in win_nummbers:
        count = 0
        for item_2 in item:
            if item_2 in choice:
                count += 1
                if count == 3:
                    return True
                else:
                    continue
            count = 0


while True:
    """Этот цикл запускаеться первым и спрашивает пользователя продолжить программу или нет"""
    start = input("""Играем? "Да" или "Нет": """).upper()
    if start != "ДА" and start != 'НЕТ':
        print('Ошиблись с вводом. Попробуйте ответить ещё раз')
        continue
    elif start == 'НЕТ':
        print('Очень жаль =(')
        break
    else:
        print('Отлично!!! Первый игрок ходит ноликами, а Второй крестиками. Первый ход за ноликами\nПоехали!!!')
        print()
        tabliza(varianti)
        break

while not pobeditel and start == 'ДА':
    """Это цикл хода первого игрока"""
    print()
    choice_1 = fahler('Первый')
    varianti.pop(choice_1)
    varianti.insert(choice_1, 'o')
    tabliza(varianti)
    igrok_1.append(str(choice_1 + 1))
    if summa(win_nummbers, igrok_1):
        pobeditel = "Первый игрок выиграл!!!"
        print()
        print()
        print(f"Итог такой - {pobeditel} Поздравляем")
        break
    while True:
        """Это цикл хода второго игрока"""
        print()
        choice_2 = fahler("Второй")
        varianti.pop(choice_2)
        varianti.insert(choice_2, 'x')
        tabliza(varianti)
        igrok_2.append(str(choice_2 + 1))
        if summa(win_nummbers, igrok_2):
            pobeditel = "Второй игрок выиграл!!!"
            print()
            print()
            print(f"Итог такой - {pobeditel} Поздравляем")
            break
        break