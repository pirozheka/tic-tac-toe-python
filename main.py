def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Проверка строк и столбцов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0], True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i], True

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0], True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2], True

    return None, False


def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        row = int(input(f"Игрок {current_player}, выберите строку (0, 1, 2): "))
        col = int(input(f"Игрок {current_player}, выберите столбец (0, 1, 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Эта клетка уже занята. Попробуйте снова.")
            continue

        winner, game_over = check_winner(board)
        if game_over:
            print_board(board)
            print(f"Игрок {winner} победил!")
            break

        if is_board_full(board):
            print_board(board)
            print("Ничья!")
            break

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


game()
