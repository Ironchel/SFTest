winner_id = 0
game_map = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
player_1_moves = []
player_2_moves = []
count_of_moves = 0
max_num_moves = 9
winning_numbers = [['1', '2', '3'],
                   ['4', '5', '6'],
                   ['7', '8', '9'],
                   ['1', '4', '7'],
                   ['2', '5', '8'],
                   ['3', '6', '9'],
                   ['1', '5', '9'],
                   ['3', '5', '7']]


def print_game_map(x):
    print(f"{x[6]} {x[7]} {x[8]}\n"
          f"{x[3]} {x[4]} {x[5]}\n"
          f"{x[0]} {x[1]} {x[2]}")


def handle_player_actions(x):
    while True:
        try:
            choice = int(input(f"{x} игрок. Выберите место (цифру): ")) - 1
            if choice < 0 or choice > 9:
                print("Не правильная цифра")
                continue
            elif game_map[choice] == 'o' or game_map[choice] == 'x':
                print("Место уже занято")
                continue
            else:
                return choice
        except:
            print("Ошибка ввода")
            continue


def check_winning_combination(choice):
    for item in winning_numbers:
        count = 0
        for item_2 in item:
            if item_2 in choice:
                count += 1
                if count == 3:
                    return True
                else:
                    continue
            count = 0

def update_game_board(player_moves, choice, move):
    game_map.pop(choice)
    game_map.insert(choice, move)
    print_game_map(game_map)
    player_moves.append(str(choice + 1))

def print_winner(winner_id):
    print()
    print()
    print(f"Итог такой - {winner_id} игрок выиграл!!! Поздравляем")

while True:
    start = input(
        """Играем? "Да" или "Нет": """).upper()  ##### тут ты спрашиваешь Да или Нет но ожидаешь ДА или НЕТ
    if start != "ДА" and start != 'НЕТ':
        print('Ошиблись с вводом. Попробуйте ответить ещё раз')
        continue
    elif start == 'НЕТ':
        print('Очень жаль =(')
        break
    else:
        print(
            'Отлично!!! Первый игрок ходит ноликами, а второй крестиками. Первый ход за ноликами\nПоехали!!!')
        print()
        print_game_map(game_map)
        break


while not winner_id and start == 'ДА' and count_of_moves != max_num_moves:
    print()
    choice_1 = handle_player_actions('Первый')
    update_game_board(player_1_moves, choice_1, 'o')
    count_of_moves += 1
    if check_winning_combination(player_1_moves):
        print_winner('Первый')
        break
    while count_of_moves != 9:
        """Это цикл хода второго игрока"""
        print()
        choice_2 = handle_player_actions("Второй")
        update_game_board(player_2_moves, choice_2, 'x')
        count_of_moves += 1
        if check_winning_combination(player_2_moves):
            print_winner('Второй')
        break
print()
if count_of_moves == 9:
    print("Победителя нет. Ничья")

