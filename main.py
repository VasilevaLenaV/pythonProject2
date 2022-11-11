# Задача 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def del_word_text(search_text, del_word):
    clear_text = list(filter(lambda x: del_word not in x, search_text.split()))
    return " ".join(clear_text)


del_template = 'абв'
in_text = input("Задача 1. Введите текст: ")
print(del_word_text(in_text, del_template))


# Задача 2. Создайте программу для игры с конфетами человек против человека.
#	Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#	Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#	Все конфеты оппонента достаются сделавшему последний ход.
#	Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint


def get_name(num):
    return input(f"Задача 2. Имя игрока {num}: ")


def get_first(players):
    step0 = randint(0, 1)
    print(f"Первым ходит  {players[step0]}")

    if step0 == 0:
        second = 1
    else:
        second = 0

    return [step0, second]


def take_step(player, balance, all_candy):
    k = input_step(player, all_candy)
    balance += k
    all_candy -= k
    info_step(player, k, balance, all_candy)
    return balance, all_candy


def input_step(name, instock):
    x = int(input(f"{name}, заберите конфеты со стола, по правилам за шаг не меньше 1 и не более 28 штук: "))
    while x < 1 or x > 28 or instock < x:
        x = int(input(f"{name}, повторите ввод кол-ва конфет: "))
    return x


def info_step(player_name, get_candy, balance_candy, last_candy):
    print(f"Игрок {player_name} сделал ход, забрал со стола {get_candy} конфет, у теперь их: {balance_candy}. на "
          f"столе осталось {last_candy} конфет.")


candy_instock = 2021
step_count = 0
balances = [0, 0]

players = [get_name(1), get_name(2)]
steps = get_first(players)

while candy_instock > 0:
    for i in steps:
        balances[i], candy_instock = take_step(players[i], balances[i], candy_instock)
        if candy_instock == 0:
            print(f"Победил игрок {players[i]} за {step_count} хода")
            break
        step_count += 1

#	a) Добавьте игру против бота

# Задача 2. Создайте программу для игры с конфетами человек против человека.
#	Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#	Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#	Все конфеты оппонента достаются сделавшему последний ход.
#	Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
#	a) Добавьте игру против бота

from random import randint


def get_name(num):
    return input(f" Задача 2. Имя игрока {num}: ")


def get_first(players):
    step0 = randint(0, 1)
    print(f"Первым ходит  {players[step0]}")

    if step0 == 0:
        second = 1
    else:
        second = 0

    return [step0, second]


def bot_step(all_take_candy):
    take_candy = 28

    if all_take_candy < 28:
        take_candy = all_take_candy

    return randint(1, take_candy)


def take_step(player, balance, all_candy, is_bot):
    if is_bot:
        k = bot_step(all_candy)
    else:
        k = input_step(player, all_candy)

    balance += k
    all_candy -= k
    info_step(player, k, balance, all_candy)
    return balance, all_candy


def input_step(name, instock):
    x = int(input(f"{name}, заберите конфеты со стола, по правилам за шаг не меньше 1 и не более 28 штук: "))
    while x < 1 or x > 28 or instock < x:
        x = int(input(f"{name}, повторите ввод кол-ва конфет: "))
    return x


def info_step(player_name, get_candy, balance_candy, last_candy):
    print(f"Игрок {player_name} сделал ход, забрал со стола {get_candy} конфет, у теперь их: {balance_candy}. на "
          f"столе осталось {last_candy} конфет.")


bot_name = "Сейлормун"
candy_instock = 2021
step_count = 0
balances = [0, 0]

players = [get_name(1), bot_name]
steps = get_first(players)

while candy_instock > 0:
    for i in steps:
        bot = i == 1
        balances[i], candy_instock = take_step(players[i], balances[i], candy_instock, bot)
        if candy_instock == 0:
            print(f"Победил игрок {players[i]} за {step_count} хода")
            break
        step_count += 1


#	b) Подумайте как наделить бота ""интеллектом""

from random import randint


def get_name(num):
    return input(f"Имя игрока {num}: ")


def get_first(players):
    step0 = randint(0, 1)
    print(f"Первым ходит  {players[step0]}")

    if step0 == 0:
        second = 1
    else:
        second = 0

    return [step0, second]


def bot_step(all_take_candy):
    take_candy = 28
    get_candy = all_take_candy % take_candy + 1

    if get_candy > take_candy:
        get_candy = randint(1, take_candy)

    if get_candy > all_take_candy:
          get_candy = randint(1, all_take_candy)
    return get_candy


def take_step(player, balance, all_candy, is_bot):
    if is_bot:
        k = bot_step(all_candy)
    else:
        k = input_step(player, all_candy)

    balance += k
    all_candy -= k
    info_step(player, k, balance, all_candy)
    return balance, all_candy


def input_step(name, instock):
    x = int(input(f"{name}, заберите конфеты со стола, по правилам за шаг не меньше 1 и не более 28 штук: "))
    while x < 1 or x > 28 or instock < x:
        x = int(input(f"{name}, повторите ввод кол-ва конфет: "))
    return x


def info_step(player_name, get_candy, balance_candy, last_candy):
    print(f"Игрок {player_name} сделал ход, забрал со стола {get_candy} конфет, у теперь их: {balance_candy}. на "
          f"столе осталось {last_candy} конфет.")


bot_name = "Сейлормун"
candy_instock = 50

players = [get_name(1), bot_name]

balances = [0, 0]
steps = get_first(players)
step_count = 0

while candy_instock > 0:
    for i in steps:
        bot = i == 1
        balances[i], candy_instock = take_step(players[i], balances[i], candy_instock, bot)
        if candy_instock == 0:
            print(f"Победил игрок {players[i]} за {step_count} хода")
            break
        step_count += 1

# Задача 3. Создайте программу для игры в ""Крестики-нолики"".
def draw_board(board):
    for i in range(3):
        print('', board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3])

        if i < 2:
            print("------------")


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for comb in win_coord:
        if board[comb[0]] == board[comb[1]] == board[comb[2]]:
            return board[comb[0]]
    return False


def get_input(input_):
    if input_.isdigit():
        if 1 <= int(input_) <= 9:
            return True

    print("Повторите ввод числа от 1 до 9 чтобы сделать ход.")
    return False


def check_pos(ppos, bboard):
    return str(bboard[ppos - 1]) not in "XO"


def take_input(player_, board_):
    valid = False
    while not valid:
        answer = input("Укажите клетку для " + player_ + "? ")

        while not get_input(answer):
            answer = input("Укажите клетку для " + player_ + "? ")

        pos = int(answer)
        valid = check_pos(pos, board_)

        if not valid:
            print("Эта клетка занята")
        else:
            board_[pos - 1] = player_
    return board_


def get_play(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            board = take_input("X", board)
        else:
            board = take_input("O", board)
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(f"\n\tИгрок {tmp}, выиграл!\n")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


get_play(list(range(1, 10)))


# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
def get_compression_rle(data):
    compression_ = ''
    count = 1

    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            count += 1
        else:
            compression_ += str(count) + data[i]
            count = 1
    if count > 1 | (data[len(data) - 2] != data[-1]):
        compression_ += str(count) + data[-1]
    return compression_


def get_uncompression_rle(undata):
    count = ''
    uncompression_ = ''
    for i in range(len(undata)):
        if not undata[i].isalpha():
            count += undata[i]
        else:
            uncompression_ += undata[i] * int(count)
            count = ''
    return uncompression_



sample_text = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'

# Подготовка файлов
# sample_text = input("Введите текст для обработки RLE алгоритмом: ")

# with open('rle_uncompress.txt', 'w') as data:
#     data.write(sample_text)
#
# with open('rle_compress.txt', 'w') as data:
#     data.write(get_compression_rle(sample_text))

# Демонстрация
with open('rle_compress.txt', 'r') as data:
    data_compress = data.read()
with open('rle_uncompress.txt', 'r') as data:
    data_uncompress = data.read()

print(f"Восстановленные данные ={get_uncompression_rle(data_compress)}")
print(f"Сжатые данные ={get_compression_rle(data_uncompress)}")