import random

def create_board():
    board = []
    for _ in range(9):
        board.append([' ']*9)
    return board

def print_board(board):
    print('  '.join([str(i) for i in range(1, 10)]))
    for row in board:
        print('  '.join(row))

def is_valid(board, column):
    if column < 0 or column > 8:
        return False
    if board[0][column] != ' ':
        return False
    return True

def find_row(board, column):
    for r in range(8, -1, -1):
        if board[r][column] == ' ':
            return r
    return None

def place_token(board, column, token):
    row = find_row(board, column)
    if row is not None:
        board[row][column] = token

def write_moves_to_file(column, token):
    with open('hamle.txt', 'a') as f:
        f.write('Oyuncu {0} {1}. sütuna taşını yerleştirdi.\n'.format(token, column+1))

def check_win(board, token):
    for row in range(9):
        for col in range(9):
            try:
                if (board[row][col] == token and 
                    board[row+1][col+1] == token and 
                    board[row+2][col+2] == token and 
                    board[row+3][col+3] == token):
                    return True
            except IndexError:
                pass
            try:
                if (board[row][col] == token and 
                    board[row+1][col] == token and 
                    board[row+2][col] == token and 
                    board[row+3][col] == token):
                    return True
            except IndexError:
                pass
            try:
                if (board[row][col] == token and 
                    board[row][col+1] == token and 
                    board[row][col+2] == token and 
                    board[row][col+3] == token):
                    return True
            except IndexError:
                pass
    return False

def game():
    board = create_board()
    game_over = False
    turn = random.randint(0, 1)
    while not game_over:
        print_board(board)
        if turn == 0:
            token = 'X'
        else:
            token = 'O'
        column = int(input('Oyuncu {0} sıra sizde. Hangi sütuna yerleştirmek istersiniz (1-9)? '.format(token))) - 1
        if is_valid(board, column):
            place_token(board, column, token)
            write_moves_to_file(column, token)
            if check_win(board, token):
                print('Oyuncu {0} kazandı!'.format(token))
                game_over = True
        turn = 1 - turn

if __name__ == "__main__":
    game()
