class Colour:                                                            
    empty = 0
    black = 1
    white = 2


class Empty:                                                            
    colour = Colour.empty

    def __str__(self):
        return '.'

    def get_moves(self, x, y, board):
        raise Exception('Error! Figure was not found')


class Chessfigure:                                                      
    img = tuple()

    def __init__ (self, colour):
        self.colour = colour

    def __str__(self):
        return self.img[0 if self.colour == Colour.black else 1]


class Pawn(Chessfigure):    #пешки
    img = ('♙', '♟')

    def get_moves(self, x, y, board):
        moves = []
        if self.colour == Colour.white:
            if y < 7 and board.get_colour(x, y + 1) == Colour.empty:
                moves.append([x, y + 1])
            if y == 1 and board.get_colour(x, y + 2) == Colour.empty:
                moves.append([x, y + 2])
            if y < 7 and 0 <= x < 7 and board.get_colour(x + 1, y + 1) == Colour.black:
                moves.append([x + 1, y + 1])
            if y < 7 and 0 < x <= 7 and board.get_colour(x - 1, y + 1) == Colour.black:
                moves.append([x - 1, y + 1])
        elif self.colour == Colour.black:
            if y > 0 and board.get_colour(x, y - 1) == Colour.empty:
                moves.append([x, y - 1])
            if y == 6 and board.get_colour(x, y - 2) == Colour.empty:
                moves.append([x, y - 2])
            if y > 0 and 0 <= x < 7 and board.get_colour(x + 1, y - 1) == Colour.white:
                moves.append([x + 1, y - 1])
            if y > 0 and 0 < x <= 7 and board.get_colour(x - 1, y - 1) == Colour.white:
                moves.append([x - 1, y - 1])
        return moves


class King(Chessfigure):    #короли
    img = ('♔', '♚')

    def get_moves(self, x, y, board):
        moves = []                                                    
        if self.colour == Colour.white:
            for _x in range(-2, 2):
                for _y in range(-2, 2):
                    if _x == 0 and _y == 0:
                        continue
                    elif _x == 2 or _x == -2:
                        if _y == 0:
                            new_x = x + _x
                            new_y = y
                            if 0 <= new_x <= 7 and \
                            board.get_colour(new_x, new_y) == Colour.empty:
                                moves.append([new_x, new_y])
                        else:
                            continue
                    elif _y == 2 or _y == -2:
                        if _x == 0:
                            new_x = x 
                            new_y = y + _y
                            if 0 <= new_y <= 7 and \
                            board.get_colour(new_x, new_y) == Colour.empty:
                                moves.append([new_x, new_y])
                        else:
                            continue
                    else:
                        new_x = x + _x
                        new_y = y + _y
                        if 0 <= new_x <= 7 and 0 <= new_y <= 7 and \
                        board.get_colour(new_x, new_y) != Colour.white:
                            moves.append([new_x, new_y])
        elif self.colour == Colour.black:
            for _x in range(-2, 2):
                for _y in range(-2, 2):
                    if _x == 0 and _y == 0:
                        continue
                    elif _x == 2 or _x == -2:
                        if _y == 0:
                            new_x = x + _x
                            new_y = y
                            if 0 <= new_x <= 7 and \
                            board.get_colour(new_x, new_y) == Colour.empty:
                                moves.append([new_x, new_y])
                        else:
                            continue
                    elif _y == 2 or _y == -2:
                        if _x == 0:
                            new_x = x 
                            new_y = y + _y
                            if 0 <= new_y <= 7 and \
                            board.get_colour(new_x, new_y) == Colour.empty:
                                moves.append([new_x, new_y])
                            else:
                                continue
                    else:
                        new_x = x + _x
                        new_y = y + _y
                        if 0 <= new_x <= 7 and 0 <= new_y <= 7 and \
                        board.get_colour(new_x, new_y) != Colour.black:
                            moves.append([new_x, new_y])
        return moves


class Knight(Chessfigure):  #кони
    img = ('♘', '♞')

    def get_moves(self, x, y, board):
        moves = []
        knight_moves = [(1,2),(2,1),(-1,2),(2,-1),(-2,1),(1,-2),(-1,-2),(-2,-1)]
        for move in knight_moves:
            new_x = x + move[0]
            new_y = y + move[1]
            if 0 <= new_x <= 7 and 0 <= new_y <= 7 and \
            board.get_colour(new_x, new_y) != self.colour:
                moves.append([new_x, new_y])
        return moves


class Bishop(Chessfigure):  #слоны
    img = ('♗', '♝')

    def get_moves(self, x, y, board):
        moves = []
        main_moves = [(-1,-1),(-1,1),(1,-1),(1,1)]
        for move in main_moves:
            a = True
            new_x = x
            new_y = y
            while a:
                new_x += move[0]
                new_y += move[1]
                if 0 <= new_x <= 7 and 0 <= new_y <= 7 and \
                board.get_colour(new_x, new_y) == Colour.empty:
                    moves.append([new_x, new_y])
                elif 0 <= new_x <= 7 and 0 <= new_y <= 7 and \
                board.get_colour(new_x, new_y) == self.colour:
                    a = False
                elif 0 <= new_x <= 7 and 0 <= new_y <= 7 and \
                board.get_colour(new_x, new_y) != self.colour:
                    moves.append([new_x, new_y])
                    a = False
                else:
                    a = False  
        return moves


class Rook(Chessfigure):    #ладьи
    img = ('♖', '♜')

    def get_moves(self, x, y, board):
        moves = []
        main_moves = [(0,1),(1,0),(-1,0),(0,-1)]
        for move in main_moves:
            a = True
            new_x = x
            new_y = y
            while a:
                new_x += move[0]
                new_y += move[1]
                if 0 <= new_x <= 7 and 0 <= new_y <= 7 and \
                board.get_colour(new_x, new_y) == Colour.empty:
                    moves.append([new_x, new_y])
                elif 0 <= new_x <= 7 and 0 <= new_y <= 7 and \
                board.get_colour(new_x, new_y) == self.colour:
                    a = False
                elif 0 <= new_x <= 7 and 0 <= new_y <= 7 and \
                board.get_colour(new_x, new_y) != self.colour:
                    moves.append([new_x, new_y])
                    a = False
                else:
                    a = False     
        return moves


class Queen(Chessfigure):   # королева, ферзь
    img = ('♕', '♛')

    def get_moves(self, x, y, board):
        moves = []
        for move1 in Rook(self.colour).get_moves( x, y, board):
            moves.append(move1) 
        for move2 in Bishop(self.colour).get_moves(x, y, board):
            moves.append(move2)
        return moves


class Board:  # шахматная доска

    def __init__ (self):
        self.desk = [[Empty() for i in range(8)] for _i in range(8)]           
        self.desk[0][0] = Rook(Colour.white)                                      
        self.desk[0][1] = Knight(Colour.white)
        self.desk[0][2] = Bishop(Colour.white)
        self.desk[0][3] = Queen(Colour.white)
        self.desk[0][4] = King(Colour.white)
        self.desk[0][5] = Bishop(Colour.white)
        self.desk[0][6] = Knight(Colour.white)
        self.desk[0][7] = Rook(Colour.white)
        self.desk[1][0] = Pawn(Colour.white)
        self.desk[1][1] = Pawn(Colour.white)
        self.desk[1][2] = Pawn(Colour.white)
        self.desk[1][3] = Pawn(Colour.white)
        self.desk[1][4] = Pawn(Colour.white)
        self.desk[1][5] = Pawn(Colour.white)
        self.desk[1][6] = Pawn(Colour.white)
        self.desk[1][7] = Pawn(Colour.white)
        self.desk[6][0] = Pawn(Colour.black)
        self.desk[6][1] = Pawn(Colour.black)
        self.desk[6][2] = Pawn(Colour.black)
        self.desk[6][3] = Pawn(Colour.black)
        self.desk[6][4] = Pawn(Colour.black)
        self.desk[6][5] = Pawn(Colour.black)
        self.desk[6][6] = Pawn(Colour.black)
        self.desk[6][7] = Pawn(Colour.black)
        self.desk[7][0] = Rook(Colour.black)
        self.desk[7][1] = Knight(Colour.black)
        self.desk[7][2] = Bishop(Colour.black)
        self.desk[7][3] = Queen(Colour.black)
        self.desk[7][4] = King(Colour.black)
        self.desk[7][5] = Bishop(Colour.black)
        self.desk[7][6] = Knight(Colour.black)
        self.desk[7][7] = Rook(Colour.black)
        self.move_point = 1

    def __str__ (self):                                                            
        resp = '    ' + 'A B C D E F G H' + '\n'
        for j, _i in enumerate(self.desk):
            resp += str(j + 1) + '  ' + ' '.join(map(str,_i)) + '  ' + str(j + 1) + '\n'
        resp += '   ' + 'A B C D E F G H'
        return resp

    def get_colour(self, x, y):                                                  
        return self.desk[y][x].colour

    def ask_moves(self, x, y):                                                      
        return self.desk[y][x].get_moves(x, y, self)

    def move(self, xy_from, xy_to):                                         
        self.desk[xy_to[1]][xy_to[0]] = self.desk[xy_from[1]][xy_from[0]]
        self.desk[xy_from[1]][xy_from[0]] = Empty()
        if self.get_colour(xy_to[0],xy_to[1]) == Colour.white:
            self.move_point += 1

    def all_moves(self, x_from, y_from):                                            
        _all = [[], []]
        for x in range(0, 7):
            for y in range(0, 7):
                if self.get_colour(x, y) == Colour.black and \
                (y != y_from or x != x_from):
                    for m in self.ask_moves(x, y):
                        _all[0].append(m)
                elif self.get_colour(x, y) == Colour.white and \
                (y != y_from or x != x_from):
                    for m in self.ask_moves(x, y):
                        _all[1].append(m)
        return _all


def translate(_str): 
    Letters = [('A',0), ('B',1), ('C',2), ('D',3), ('E',4), ('F',5), ('G',6), ('H',7)]
    _str = list(_str)
    if len(_str) != 2:
        raise ValueError('Error, a lot of symbols')        
    else:
        new_str = [None, None]
        for i in range(2):
            try:
                _str[i] = int(_str[i])
            except ValueError:
                for value in Letters:
                    if _str[i] == value[0]:
                        new_str[0] = value[1]
            else:
                _str[i] += -1
                new_str[1] = _str[i]
    if  new_str[0] == None or new_str[1] > 7 or new_str[1] < 0:
        raise TypeError('Error, another symbols')
    return new_str
