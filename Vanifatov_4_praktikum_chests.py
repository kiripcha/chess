#Ванифатов ПИ20-5 1,2,8 задания + основная часть = 10 баллов 
import os #для комфортной работы с файлами
field = [['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']]
figures = [['r', 1, 1, 0], ['n', 1, 2, 0], ['b', 1, 3, 0], ['q', 1, 4, 0], ['k', 1, 5, 0], ['b', 1, 6, 0],
           ['n', 1, 7, 0], ['r', 1, 8, 0], ['p', 2, 1, 0], ['p', 2, 2, 0], ['p', 2, 3, 0], ['p', 2, 4, 0],
           ['p', 2, 5, 0], ['p', 2, 6, 0], ['p', 2, 7, 0], ['p', 2, 8, 0], ['R', 8, 1, 1], ['N', 8, 2, 1],
           ['B', 8, 3, 1], ['Q', 8, 4, 1], ['K', 8, 5, 1], ['B', 8, 6, 1], ['N', 8, 7, 1], ['R', 8, 8, 1],
           ['P', 7, 1, 1], ['P', 7, 2, 1], ['P', 7, 3, 1], ['P', 7, 4, 1], ['P', 7, 5, 1], ['P', 7, 6, 1],
           ['P', 7, 7, 1], ['P', 7, 8, 1]]
kontrol = True
pr_turn =[]


def which_colour(x, y): # определение цвета
    for i in range(len(figures)):
        if figures[i][1] == x and figures[i][2] == y:
            return figures[i][3]


def delete_figure(x, y): # удаление фигуры
    for i in range(len(figures)):
        if figures[i][1] == x and figures[i][2] == y:
            if figures[i][0] == 'k' or figures[i][0] == 'K':
                global kontrol
                kontrol = False
            figures[i][1] = -1
            figures[i][2] = -1


def print_field():  # выводит поле на экран
    print('    A B C D E F G H')
    print('    _______________')
    for i in range(len(field)):
        print(8 - i, '|', end=' ')
        for j in range(len(field[i])):
            print(field[i][j], end=' ')
        print('|', 8 - i)
    print('    _______________')
    print('    A B C D E F G H')


def place_figure(x1, x2, y1, y2):  # меняет координаты фигуры
    for i in range(len(figures)):
        if figures[i][1] == x1 and figures[i][2] == y1:
            figures[i][1] = x2
            figures[i][2] = y2


def clear_way(x, y):  # проверяет пустая ли клетка с переданными координатами
    for i in range(len(figures)):
        if figures[i][1] == x and figures[i][2] == y:
            return False
    return True


def pawn(x1, y1, x2, y2, colour): # отвечает за передвижение пешок
    k = 1
    count = 0
    if y2 == y1 and abs(x2 - x1) == 1:
        if clear_way(x2, y2):
            place_figure(x1, x2, y1, y2)
        return True
    elif y2 == y1 and x2 - x1 == 2 and x1 == 2: # проверка для белых
        while k < 3:
            if clear_way(x1 + k, y1):
                count += 1
            k += 1
        if count == 2:
            place_figure(x1, x2, y1, y2)
        return True
    elif y2 == y1 and x1 - x2 == 2 and x1 == 7: # проверка для черных
        while k < 3:
            if clear_way(x1 - k, y1):
                count += 1
            k += 1
        if count == 2:
            place_figure(x1, x2, y1, y2)
        return True
    elif (y2 == y1 + 1 or y2 == y1 - 1) and abs(x2 - x1) == 1: # ест фигуру
        if not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
    #elif                                                            #ВЗЯТИЕ НА ПРОХОДЕ
        return True
    else:# иначе остается на месте
        return False


def rook(x1, y1, x2, y2, colour):  # отвечает за перемещение ладьей
    k = 1
    count = 0
    if y1 == y2 and x2 > x1: # ход ладьи по горизонтали(строчкам) вправо
        while k < (x2-x1 + 1):
            if clear_way(x1+k, y1):
                count += 1
            k += 1
        if count == x2-x1:
            place_figure(x1, x2, y1, y2)
        elif count == x2 - x1 - 1 and not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif y1 == y2 and x1 > x2: # ход ладьи по горизонтали(строчкам) влево
        while k < (x1-x2 + 1):
            if clear_way(x1-k, y1):
                count += 1
            k += 1
        if count == x1-x2:
            place_figure(x1, x2, y1, y2)
        elif count == x1 - x2 - 1 and not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 == x1 and y2 > y1: # ход ладьи по вертикали(столбцам) вверх
        while k < (y2 - y1) + 1:
            if clear_way(x1, y1+k):
                count += 1
            k += 1
        if count == y2 - y1:
            place_figure(x1, x2, y1, y2)
        elif count == y2 - y1 - 1 and not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 == x1 and y1 > y2: # ход ладьи по вертикали(столбцам) вниз
        while k < (y1 - y2) + 1:
            if clear_way(x1, y1 - k):
                count += 1
            k += 1
        if count == y1 - y2:
            place_figure(x1, x2, y1, y2)
        elif count == y1 - y2 - 1 and not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    else:# иначе остается на месте
        return False


def bishop(x1, y1, x2, y2, colour): # отвечает за перемещение слонов
    k = 1
    count = 0
    if x2 > x1 and y2 > y1: # по диагонали вверх вправо
        while k < (y2 - y1) + 1:
            if clear_way(x1 + k, y1 + k):
                count += 1
            k += 1
        if count == y2 - y1:
            place_figure(x1, x2, y1, y2)
        elif count == y2 - y1 - 1 and not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 > x1 and y1 > y2: # по диагонали вверх влево
        while k < (y1 - y2) + 1:
            if clear_way(x1 + k, y1 - k):
                count += 1
            k += 1
        if count == y1 - y2:
            place_figure(x1, x2, y1, y2)
        elif count == y1 - y2 - 1 and not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x1 > x2 and y2 > y1: # по диагонали вниз вправо
        while k < (y2 - y1) + 1:
            if clear_way(x1 - k, y1 + k):
                count += 1
            k += 1
        if count == y2 - y1:
            place_figure(x1, x2, y1, y2)
        elif count == y2 - y1 - 1 and not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x1 > x2 and y1 > y2: # по диагонали вниз влево
        while k < (y1 - y2) + 1:
            if clear_way(x1 - k, y1 - k):
                count += 1
            k += 1
        if count == y1 - y2:
            place_figure(x1, x2, y1, y2)
        elif count == y1 - y2 - 1 and not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    else: # иначе остается на месте
        return False


def knight(x1, y1, x2, y2, colour): # отвечает за перемещение коня
    if x2 == x1+2 and y2 == y1+1:
        if clear_way(x2, y2):
            place_figure(x1, x2, y1, y2)
        else:
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 == x1+2 and y2 == y1-1:
        if clear_way(x2, y2):
            place_figure(x1, x2, y1, y2)
        else:
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 == x1-2 and y2 == y1-1:
        if clear_way(x2, y2):
            place_figure(x1, x2, y1, y2)
        else:
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 == x1-2 and y2 == y1+1:
        if clear_way(x2, y2):
            place_figure(x1, x2, y1, y2)
        else:
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 == x1-1 and y2 == y1+2:
        if clear_way(x2, y2):
            place_figure(x1, x2, y1, y2)
        else:
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 == x1-1 and y2 == y1-2:
        if clear_way(x2, y2):
            place_figure(x1, x2, y1, y2)
        else:
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 == x1+1 and y2 == y1+2:
        if clear_way(x2, y2):
            place_figure(x1, x2, y1, y2)
        else:
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 == x1+1 and y2 == y1-2:
        if clear_way(x2, y2):
            place_figure(x1, x2, y1, y2)
        else:
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    else:
        return False


def queen(x1, y1, x2, y2, colour): # отвечает за передвижение ферзя
    k = 1
    count = 0
    if y1 == y2 and x2 > x1: #передвижение вертикально вверх
        while k < (x2 - x1 + 1):
            if clear_way(x1 + k, y1):
                count += 1
            k += 1
        if count == x2 - x1:
            place_figure(x1, x2, y1, y2)
        elif count == x2 - x1 - 1 and not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif y1 == y2 and x1 > x2: #передвижение вертикально вниз
        while k < (x1 - x2 + 1):
            if clear_way(x1 - k, y1):
                count += 1
            k += 1
        if count == x1 - x2:
            place_figure(x1, x2, y1, y2)
        elif count == x1 - x2 - 1 and not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 == x1 and y2 > y1: #передвижение горизонтально вправо
        while k < (y2 - y1) + 1:
            if clear_way(x1, y1 + k):
                count += 1
            k += 1
        if count == y2 - y1:
            place_figure(x1, x2, y1, y2)
        elif count == y2 - y1 - 1 and not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 == x1 and y1 > y2: #передвижение горизонтально влево
        while k < (y1 - y2) + 1:
            if clear_way(x1, y1 - k):
                count += 1
            k += 1
        if count == y1 - y2:
            place_figure(x1, x2, y1, y2)
        elif count == y1 - y2 - 1 and not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 > x1 and y2 > y1: #по диагонали вверх вправо
        while k < (y2 - y1) + 1:
            if clear_way(x1 + k, y1 + k):
                count += 1
            k += 1
        if count == y2 - y1:
            place_figure(x1, x2, y1, y2)
        elif count == y2 - y1 - 1 and not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 > x1 and y1 > y2: #по диагонали вверх влево
        while k < (y1 - y2) + 1:
            if clear_way(x1 + k, y1 - k):
                count += 1
            k += 1
        if count == y1 - y2:
            place_figure(x1, x2, y1, y2)
        elif count == y1 - y2 - 1 and not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x1 > x2 and y2 > y1: #по диагонали вниз вправо
        while k < (y2 - y1) + 1:
            if clear_way(x1 - k, y1 + k):
                count += 1
            k += 1
        if count == y2 - y1:
            place_figure(x1, x2, y1, y2)
        elif count == y2 - y1 - 1 and not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x1 > x2 and y1 > y2: #по диагонали вниз вправо
        while k < (y1 - y2) + 1:
            if clear_way(x1 - k, y1 - k):
                count += 1
            k += 1
        if count == y1 - y2:
            place_figure(x1, x2, y1, y2)
        elif count == y1 - y2 - 1 and not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    else:
        return False


def king(x1, y1, x2, y2, colour): # отвечает за передвижение короля
    if y1 == y2 and x2 == x1 + 1: #по вертикали вверх
        if clear_way(x2, y2):
            place_figure(x1, x2, y1, y2)
        elif not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif y1 == y2 and x2 == x1 - 1: #по вертикали вниз
        if clear_way(x2, y2):
            place_figure(x1, x2, y1, y2)
        elif not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 == x1 and y2 == y1 + 1: #по горизонтали вправо
        if clear_way(x2, y2):
            place_figure(x1, x2, y1, y2)
        elif not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 == x1 and y2 == y1 - 1: #по горизонтали влево
        if clear_way(x2, y2):
            place_figure(x1, x2, y1, y2)
        elif not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 == x1 + 1 and y2 == y1 + 1: # по диагонали вверх вправо
        if clear_way(x2, y2):
            place_figure(x1, x2, y1, y2)
        elif not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 == x1 + 1 and y2 == y1 - 1: #по диагонали вверх влево
        if clear_way(x2, y2):
            place_figure(x1, x2, y1, y2)
        elif not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 == x1 - 1 and y2 == y1 + 1: #по диагонали вниз вправо 
        if clear_way(x2, y2):
            place_figure(x1, x2, y1, y2)
        elif not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x2 == x1 - 1 and y2 == y1 - 1: #по диагонали вниз влево
        if clear_way(x2, y2):
            place_figure(x1, x2, y1, y2)
        elif not clear_way(x2, y2):
            op_colour = which_colour(x2, y2)
            if op_colour != colour:
                delete_figure(x2, y2)
                place_figure(x1, x2, y1, y2)
        return True
    elif x1 == x2 and y1 == y2 - 2: # короткая рокировка
        if clear_way(x1, y1+1) and clear_way(x1, y1+2):
            for i in range(len(figures)):
                if figures[i][1] == x1 and figures[i][2] == y2+1 and (figures[i][0] == 'r' or figures[i][0] == 'R'):
                    place_figure(x1, x2, y1, y2)
                    place_figure(x2, x1, y2+1, y1+1)
        return True
    elif x1 == x2 and y1 == y2 + 3: #длинная рокировка
        if clear_way(x1, y2) and clear_way(x1, y2+1) and clear_way(x1, y2+2):
            for i in range(len(figures)):
                if figures[i][1] == x1 and figures[i][2] == y2-1 and (figures[i][0] == 'r' or figures[i][0] == 'R'):
                    place_figure(x1, x2, y1, y2)
                    place_figure(x2, x1, y2-1, y1-2)
        return True
    else:
        return False


def checking_for_move(x, y, colour, type_figure): #проверка передвижения фигур
    if colour == 0:
        for i in range(1, 16):
            if type_figure == 'p' and figures[i][0] == 'p':
                if pawn(figures[i][1], figures[i][2], x, y, 0):
                    pr_turn.append(figures[i][1])
                    pr_turn.append(figures[i][2])
            elif type_figure == 'r' and figures[i][0] == 'r':
                rook(figures[i][1], figures[i][2], x, y, 0)
            elif type_figure == 'b' and figures[i][0] == 'b':
                bishop(figures[i][1], figures[i][2], x, y, 0)
            elif type_figure == 'n' and figures[i][0] == 'n':
                knight(figures[i][1], figures[i][2], x, y, 0)
            elif type_figure == 'q' and figures[i][0] == 'q':
                queen(figures[i][1], figures[i][2], x, y, 0)
            elif type_figure == 'k' and figures[i][0] == 'k':
                king(figures[i][1], figures[i][2], x, y, 0)
    elif colour == 1:
        for i in range(len(figures)):
            if type_figure == 'P' and figures[i][0] == 'P':
                pawn(figures[i][1], figures[i][2], x, y, 1)
            elif type_figure == 'R' and figures[i][0] == 'R':
                rook(figures[i][1], figures[i][2], x, y, 1)
            elif type_figure == 'B' and figures[i][0] == 'B':
                bishop(figures[i][1], figures[i][2], x, y, 1)
            elif type_figure == 'N' and figures[i][0] == 'N':
                knight(figures[i][1], figures[i][2], x, y, 1)
            elif type_figure == 'Q' and figures[i][0] == 'Q':
                queen(figures[i][1], figures[i][2], x, y, 1)
            elif type_figure == 'K' and figures[i][0] == 'K':
                king(figures[i][1], figures[i][2], x, y, 1)


def main(move_number=0): # меню шахматной партии                                                  
    prov = False
    temp = False
    dict_input = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    x1 = x2 = y1 = y2 = 0
    while kontrol:
        for i in range(len(field)):
            for j in range(len(field[i])):
                field[i][j] = '.'
        for i in range(len(figures)):
            i1 = figures[i][1] - 1
            j1 = figures[i][2] - 1
            if i1 != -2 and j1 != -2:
                field[i1][j1] = figures[i][0]
        # os.system('cls')
        print_field()
        print('сделанно ходов: ', move_number)
        if move_number % 2 == 0:
            print('ХОД БЕЛЫХ')
            colour = 0
        else:
            print('ХОД ЧЕРНЫХ')
            colour = 1
        while not prov:
            while not prov:
                try:
                    print('Введите номер столбца фигуры, куда хотите сходить:')
                    try:
                        y1_t = input()
                        y1 = dict_input.setdefault(y1_t)
                    except ValueError:
                        print('Введены неверные данные, попробуйте еще раз')
                        temp = True
                    if not temp:
                        assert y1 > 0, 'Введены неверные данные, попробуйте еще раз, они не попадают в диапазон поля'
                        assert y1 < 9, 'Введены неверные данные, попробуйте еще раз, они не попадают в диапазон поля'
                        prov = True
                except AssertionError as err:
                    print(err)
                temp = False
            prov = False
            try:
                print('Введите номер строки фигуры, которой хотите сходить:')
                try:
                    x1 = 9 - int(input())
                except ValueError:
                    print('Введены неверные данные, попробуйте еще раз')
                    temp = True
                if not temp:
                    assert x1 > 0, 'Введены неверные данные, попробуйте еще раз, они не попадают в диапазон поля'
                    assert x1 < 9, 'Введены неверные данные, попробуйте еще раз, они не попадают в диапазон поля'
                    prov = True
            except AssertionError as err:
                print(err)
            temp = False
        prov = False
        while not prov:
            try:
                print('Введите номер столбца фигуры, куда хотите сходить:')
                try:
                    y2_t = input()
                    y2 = dict_input.setdefault(y2_t)
                except ValueError:
                    print('Введены неверные данные, попробуйте еще раз')
                    temp = True
                if not temp:
                    assert y2 > 0, 'Введены неверные данные, попробуйте еще раз, они не попадают в диапазон поля'
                    assert y2 < 9, 'Введены неверные данные, попробуйте еще раз, они не попадают в диапазон поля'
                    prov = True
            except AssertionError as err:
                print(err)
            temp = False
        prov = False
        while not prov:
            try:
                print('Введите номер строки фигуры, куда хотите сходить:')
                try:
                    x2 = 9 - int(input())
                except ValueError:
                    print('Введены неверные данные, попробуйте еще раз')
                    temp = True
                if not temp:
                    assert x2 > 0, 'Введены неверные данные, попробуйте еще раз, они не попадают в диапазон поля'
                    assert x2 < 9, 'Введены неверные данные, попробуйте еще раз, они не попадают в диапазон поля'
                    prov = True
            except AssertionError as err:
                print(err)
            temp = False
        prov = False
        for i in range(len(figures)):
            if figures[i][1] == x1 and figures[i][2] == y1:
                type_figure = figures[i][0]
                if type_figure == 'p' or type_figure == 'P':
                    if figures[i][3] == 0:
                        if not pawn(x1, y1, x2, y2, 0):
                            move_number -= 1
                    else:
                        pawn(x1, y1, x2, y2, 1)
                elif type_figure == 'r' or type_figure == 'R':
                    if figures[i][3] == 0:
                        if not rook(x1, y1, x2, y2, 0):
                            move_number -= 1
                    else:
                        rook(x1, y1, x2, y2, 1)
                elif type_figure == 'b' or type_figure == 'B':
                    if figures[i][3] == 0:
                        if not bishop(x1, y1, x2, y2, 0):
                            move_number -= 1
                    else:
                        bishop(x1, y1, x2, y2, 1)
                elif type_figure == 'n' or type_figure == 'N':
                    if figures[i][3] == 0:
                        if not knight(x1, y1, x2, y2, 0):
                            move_number -= 1
                    else:
                        knight(x1, y1, x2, y2, 1)
                elif type_figure == 'q' or type_figure == 'Q':
                    if figures[i][3] == 0:
                        if not queen(x1, y1, x2, y2, 0):
                            move_number -= 1
                    else:
                        queen(x1, y1, x2, y2, 1)
                elif type_figure == 'k' or type_figure == 'K':
                    if figures[i][3] == 0:
                        if not king(x1, y1, x2, y2, 0):
                            move_number -= 1
                    else:
                        king(x1, y1, x2, y2, 1)
        if not kontrol:
            print('вы проиграли, Ваш король пал')
        else:
            move_number += 1
    # os.system('pause')


def notation_full(): # полная нотация ходов всей партии
    try:
        print('Введите название файла')
        file = input()
        with open(file, 'r', encoding='utf-8') as f:
            data = []
            count = 0
            new_data = []
            fig_names = ['N', 'K', 'Q', 'B', 'R']
            for row in f:
                data.append(row)
            for i in range(len(data)):
                if i != len(data) - 1:
                    data[i] = data[i][3:-1]
                else:
                    data[i] = data[i][3:]
            # print(data)
            for i in range(len(data)):
                new_data.append(data[i].split(' '))
            # print(new_data)
            for i in range(len(new_data)):
                for j in range(len(new_data[i])):
                    for z in range(len(fig_names)):
                        if new_data[i][j][0] == fig_names[z]:
                            new_data[i][j] = new_data[i][j][1:]
            # print(new_data)
        dict_field = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        turn = 1
        move_number = 0
        prov = False
        while count < len(new_data):
            print('нажмите 1, если хотите посмотреть следующий ход\n'
                  'нажмите 2, если хотите посмотреть предыдущий ход\n'
                  'нажмите 3, если хотите перейти в режим игры')
            while not prov:
                try:
                    turn = int(input())
                    prov = True
                except ValueError:
                    print('введите одно из трех значений')
            prov = False
            if turn == 1:
                print('ХОД БЕЛЫХ')
                x1 = 9 - int(new_data[move_number][0][1])
                y1 = dict_field.setdefault(new_data[move_number][0][0])
                x2 = 9 - int(new_data[move_number][0][4])
                y2 = dict_field.setdefault(new_data[move_number][0][3])
                # print(x1, y1, x2, y2)
                if new_data[move_number][0][2] == '—':
                    place_figure(x1, x2, y1, y2)
                elif new_data[move_number][0][2] == 'x':
                    delete_figure(x2, y2)
                    place_figure(x1, x2, y1, y2)
                for i in range(len(field)):
                    for j in range(len(field[i])):
                        field[i][j] = '.'
                for i in range(len(figures)):
                    i1 = figures[i][1] - 1
                    j1 = figures[i][2] - 1
                    if i1 != -2 and j1 != -2:
                        field[i1][j1] = figures[i][0]
                print_field()
                try:
                    x1 = 9 - int(new_data[move_number][1][1])
                    y1 = dict_field.setdefault(new_data[move_number][1][0])
                    x2 = 9 - int(new_data[move_number][1][4])
                    y2 = dict_field.setdefault(new_data[move_number][1][3])
                except IndexError:
                    print('МАТ, конец партии')
                    return 0
                print('ХОД ЧЕРНЫХ')
                # print(x1, y1, x2, y2)
                place_figure(x1, x2, y1, y2)
                for i in range(len(field)):
                    for j in range(len(field[i])):
                        field[i][j] = '.'
                for i in range(len(figures)):
                    i1 = figures[i][1] - 1
                    j1 = figures[i][2] - 1
                    if i1 != -2 and j1 != -2:
                        field[i1][j1] = figures[i][0]
                # os.system('cls')
                print_field()
                move_number += 1
                count += 1
            elif turn == 2 and move_number > 0:
                move_number -= 1
                print('ХОД ЧЕРНЫХ')
                x1 = 9 - int(new_data[move_number][0][1])
                y1 = dict_field.setdefault(new_data[move_number][0][0])
                x2 = 9 - int(new_data[move_number][0][4])
                y2 = dict_field.setdefault(new_data[move_number][0][3])
                # print(x1, y1, x2, y2)
                if new_data[move_number][0][2] == '—':
                    place_figure(x2, x1, y2, y1)
                elif new_data[move_number][0][2] == 'x':
                    delete_figure(x2, y2)
                    place_figure(x2, x1, y2, y1)
                for i in range(len(field)):
                    for j in range(len(field[i])):
                        field[i][j] = '.'
                for i in range(len(figures)):
                    i1 = figures[i][1] - 1
                    j1 = figures[i][2] - 1
                    if i1 != -2 and j1 != -2:
                        field[i1][j1] = figures[i][0]
                print_field()
                try:
                    x1 = 9 - int(new_data[move_number][1][1])
                    y1 = dict_field.setdefault(new_data[move_number][1][0])
                    x2 = 9 - int(new_data[move_number][1][4])
                    y2 = dict_field.setdefault(new_data[move_number][1][3])

                except IndexError:
                    print('МАТ, конец партии')
                    return 0
                print('ХОД БЕЛЫХ')
                # print(x1, y1, x2, y2)
                place_figure(x2, x1, y2, y1)
                for i in range(len(field)):
                    for j in range(len(field[i])):
                        field[i][j] = '.'
                for i in range(len(figures)):
                    i1 = figures[i][1] - 1
                    j1 = figures[i][2] - 1
                    if i1 != -2 and j1 != -2:
                        field[i1][j1] = figures[i][0]
                # os.system('cls')
                print_field()
                count -= 1
            elif turn == 2 and move_number == 0:
                print('Нет предыдущих ходов')
            elif turn == 3:
                main(move_number)
    except FileNotFoundError:
        print('Файл не найден')


def short_notation(): # короткая нотация ходов всей партии
    try:
        print('Введите название файла')
        file = input()
        dict_field = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        count = 0
        with open(file, 'r', encoding='utf-8') as f:
            data = []
            new_data = []
            for row in f:
                data.append(row)
            for i in range(len(data)):
                if i != len(data) - 1:
                    data[i] = data[i][3:-1]
                else:
                    data[i] = data[i][3:]
            # print(data)
            for i in range(len(data)):
                new_data.append(data[i].split(' '))
            # print(new_data)
        ts = ''
        ii = 0
        jj = 0
        for i in range(len(new_data)):
            for j in range(len(new_data[i])):
                for z in range(len(new_data[i][j])):
                    if new_data[i][j][z] == 'x':
                        pos = z
                        ts = new_data[i][j][0: pos] + new_data[i][j][pos+1:]
                        ii = i
                        jj = j
        new_data[ii][jj] = ts
        print(new_data)
        prov = False
        turn = 0
        move_number = 0
        while count < len(new_data):
            print('нажмите 1, если хотите посмотреть следующий ход\n'
                  'нажмите 2, если хотите посмотреть предыдущий ход\n'
                  'нажмите 3, если хотите перейти в режим игры')
            while not prov:
                try:
                    turn = int(input())
                    prov = True
                except ValueError:
                    print('введите одно из трех значений')
            prov = False
            if turn == 1:
                print('ХОД БЕЛЫХ')
                if len(new_data[move_number][0]) == 2:
                    x = 9 - int(new_data[move_number][0][1])
                    y = dict_field.setdefault(new_data[move_number][0][0])
                    checking_for_move(x, y, 1, 'P')
                if len(new_data[move_number][0]) >= 3:
                    if new_data[move_number][0][0] == 'N':
                        x = 9 - int(new_data[move_number][0][2])
                        y = dict_field.setdefault(new_data[move_number][0][1])
                        checking_for_move(x, y, 1, 'N')
                    elif new_data[move_number][0][0] == 'R':
                        x = 9 - int(new_data[move_number][0][2])
                        y = dict_field.setdefault(new_data[move_number][0][1])
                        checking_for_move(x, y, 1, 'R')
                    elif new_data[move_number][0][0] == 'Q':
                        x = 9 - int(new_data[move_number][0][2])
                        y = dict_field.setdefault(new_data[move_number][0][1])
                        checking_for_move(x, y, 1, 'Q')
                    elif new_data[move_number][0][0] == 'K':
                        x = 9 - int(new_data[move_number][0][2])
                        y = dict_field.setdefault(new_data[move_number][0][1])
                        checking_for_move(x, y, 1, 'K')
                    elif new_data[move_number][0][0] == 'B':
                        x = 9 - int(new_data[move_number][0][2])
                        y = dict_field.setdefault(new_data[move_number][0][1])
                        checking_for_move(x, y, 1, 'B')
                for i in range(len(field)):
                    for j in range(len(field[i])):
                        field[i][j] = '.'
                for i in range(len(figures)):
                    i1 = figures[i][1] - 1
                    j1 = figures[i][2] - 1
                    if i1 != -2 and j1 != -2:
                        field[i1][j1] = figures[i][0]
                print_field()
                try:
                    if len(new_data[move_number][1]) == 2:
                        x = 9 - int(new_data[move_number][1][1])
                        y = dict_field.setdefault(new_data[move_number][1][0])
                        checking_for_move(x, y, 0, 'p')
                    if len(new_data[move_number][1]) >= 3:
                        if new_data[move_number][1][0] == 'N':
                            x = 9 - int(new_data[move_number][1][2])
                            y = dict_field.setdefault(new_data[move_number][1][1])
                            checking_for_move(x, y, 0, 'n')
                        elif new_data[move_number][1][0] == 'R':
                            x = 9 - int(new_data[move_number][1][2])
                            y = dict_field.setdefault(new_data[move_number][1][1])
                            checking_for_move(x, y, 0, 'r')
                        elif new_data[move_number][1][0] == 'Q':
                            x = 9 - int(new_data[move_number][1][2])
                            y = dict_field.setdefault(new_data[move_number][1][1])
                            checking_for_move(x, y, 0, 'q')
                        elif new_data[move_number][1][0] == 'K':
                            x = 9 - int(new_data[move_number][1][2])
                            y = dict_field.setdefault(new_data[move_number][1][1])
                            checking_for_move(x, y, 0, 'k')
                        elif new_data[move_number][1][0] == 'B':
                            x = 9 - int(new_data[move_number][1][2])
                            y = dict_field.setdefault(new_data[move_number][1][1])
                            checking_for_move(x, y, 0, 'b')
                except IndexError:
                    print('МАТ, конец партии')
                    return 0
                print('ХОД ЧЕРНЫХ')
                for i in range(len(field)):
                    for j in range(len(field[i])):
                        field[i][j] = '.'
                for i in range(len(figures)):
                    i1 = figures[i][1] - 1
                    j1 = figures[i][2] - 1
                    if i1 != -2 and j1 != -2:
                        field[i1][j1] = figures[i][0]
                print_field()
                move_number += 1
                count += 1
            elif turn == 3:
                main(move_number)
    except FileNotFoundError:
        print('Такой файл не найден')


print('Если вы хотите сыграть партию введите 1\n'
      'Если хотите посмотреть партию по полной шахматной нотации нажмите 2\n'
      'Если хотите посмотреть партию по упрощенной шахматной нотации нажмите 3')
what_to_do = int(input())
if what_to_do == 1:
    main()
elif what_to_do == 2:
    notation_full()
elif what_to_do == 3:
    short_notation()
