import board

class Writes:                                                              
    stand = 'позиция фигуры: '
    move = 'новое поле: '
    wrong_move = 'ход невозможен'
    a_lot_symb = "слишком много символов"
    wrong_symb = 'неверные символы'
    wrong_stand = 'вы не можете ходить чужими фигурами или пустыми клетками'
    impossible_move = 'у фигуры нет доступных ходов'
    already_be = 'вы не можете ставить фигуру на то место, где уже стоит ваша фигура'

def clear_screen():                                                       
    from os import system, name
    system('cls' if name == 'nt' else 'clear')

def turns_counts(board, white_step):                                      
    return f"{board.move_point} ход {'белых' if white_step else 'черных'}."

def get_coordinates(invite, white_step):                                   
    while True:                                                            
        try:
            coordinates = board.translate(input(invite))
        except ValueError:
            print(Writes.a_lot_symb)
        except TypeError:
            print(Writes.wrong_symb)
        else:
            x = coordinates[0]
            y = coordinates[1]
            if white_step:
                _colour = board.Colour.white
            else:
                _colour = board.Colour.black
            if desk.get_colour(x, y) != _colour:
                print(Writes.wrong_stand)
            elif desk.ask_moves(x, y) == []:
                print(Writes.impossible_move)
            else:
                break
    return coordinates

def move_target(invite, coordinates, white_step):                               
    while True:                                                                 
        try:
            xy_to = board.translate(input(invite))
        except ValueError:
            print(Writes.a_lot_symb)
        except TypeError:
            print(Writes.wrong_symb)
        else:
            x = xy_to[0]
            y = xy_to[1]
            colors = [board.Colour.empty]
            if white_step:
                colors.append(board.Colour.black)
            else:
                colors.append(board.Colour.white)
            if desk.get_colour(x, y) not in colors:
                print(Writes.already_be)
            elif xy_to not in desk.ask_moves(coordinates[0], coordinates[1]):
                print(Writes.wrong_move)
            else:
                break
    return xy_to

white_step = False
desk = board.Board()

clear_screen()
while True:                                                                  
    print(desk)
    print(turns_counts(desk, white_step))
    xy_from = get_coordinates(Writes.stand, white_step)
    xy_to = move_target(Writes.move, xy_from, white_step)                      
    desk.move(xy_from, xy_to)
    white_step = not white_step
    clear_screen()
