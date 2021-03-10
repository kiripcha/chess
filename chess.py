class Colour(object):
    empty = 0
    black = 1
    white = 2

class Empty(object):
    colour = Colour.empty

    def get_moves(self, board, x, y):
        raise Exception(' !Erorr! You move a nonexistent figure!')

    def __repr__(self):
        return ' ' # write instead of empty figure

class ChessMan(object):
    img = None

    def __init__(self, colour):
        self.colour = colour

    def __repr__(self):
        return self.img[0 if self.colour == Colour.black else 1]


class Pawn(ChessMan):
    img = ('♙','♟')

    def get_moves(self, board, x, y):
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


class King(ChessMan):
    img = ('♔','♚')

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

class Knight(ChessMan):
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

class Bishop(ChessMan):  #слоны
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

class Rook(ChessMan):    #ладьи
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

class Queen(ChessMan):   # королева, ферзь
    img = ('♕', '♛')

    def get_moves(self, x, y, board):
        moves = []
        for move1 in Rook(self.colour).get_moves( x, y, board):
            moves.append(move1) 
        for move2 in Bishop(self.colour).get_moves(x, y, board):
            moves.append(move2)
        return moves

class Board(object):
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

    def get_colour(self, x, y):
        return self.board[y][x].colour

    def get_moves(self, x, y):
        return self.board[y][x].get_moves(self, x, y)

    def move(self, xy_from, xy_to):
        self.board[xy_to[1]][xy_to[0]] = self.board[xy_from[1]][xy_from[0]]
        self.board[xy_from[1]][xy_from[0]] = Empty()

    def __str__(self):
        colours = [44,41] # цвета ячеек доски
        res = ''
        i = 0
        for y in range(8):
            for x in range(8):
                res += set_colour(colours[i]) + str(self.board[y][x]) + '  '
                i = 1 - i
            i = 1 - i
            res += set_colour(0) + '\n' # output ChessBoard per string
        return res

# colourful board
def set_colour(colour): 
    return '\033[%sm' % colour

print(Board())
Board().move([2,1], Board().get_moves(2,1)[0])
print(Board())