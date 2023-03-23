import re
import sys

LENGTH = 6

rows = ['a', 'b', 'c', 'd', 'e', 'f']
letter_to_num = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}


class Player:
    def __init__(self, name, team):
        self._name = name
        self.score = 0
        self.team = team

    @property
    def name(self):
        return self._name


def main():
    board = create_board()
    # Setting up the players
    name1 = get_name()
    name2 = get_name()
    p1 = Player(name1, 'offense')
    p2 = Player(name2, 'defense')
    play_move(board, p1, True)
    for i in range(17):
        if not check_possible(board, p1):
            end_game(board, p1, p2)
            break
        play_move(board, p1, False)
        play_move(board, p2, False)
        check_score(board, p1, p2)
        check_score(board, p2, p1)
        print_board(board, p1, p2)
    if not check_possible(board, p1):
        end_game(board, p1, p2)
    play_move(board, p1, False)
    end_game(board, p1, p2)


# Initializing the board
def create_board():
    board = []
    for i in range(LENGTH):
        row = []
        for column in range(LENGTH):
            row.append(' ')
        board.append(row)
    return board


def get_name():
    # Getting 1 letter name
    while True:
        try:
            name = input("Name: ").strip()
            if re.search(r'^[a-zA-Z]$', name):
                return name
            else:
                raise ValueError
        except ValueError:
            print("Must be 1 letter")
            pass


# Prints out the board to the console using ASCII Art
def print_board(board, p1, p2):
    print("\n\n\n")
    print("|--" + "-|--" * 5 + "-|")
    for row in board:
        print("| ", end='')
        for square in row:
            print(square + " | ", end='')
        print()
        print("|--" + "-|--" * 5 + "-|")
    print()
    print(p1.name + "'s Score: " + str(p1.score))
    print(p2.name + "'s Score: " + str(p2.score))
    print('\n\n\n')


# Checking if offense can make a move
def check_possible(board, p1):
    for i in range(6):
        for j in range(6):
            # Checking board for squares that have offense
            if board[i][j] == p1.name:
                # Top edge
                if i == 0:
                    # Literal top left corner case
                    if j == 0:
                        if board[i][j + 1] == ' ' or board[i + 1][j] == ' ' or board[i + 1][j + 1] == ' ':
                            return True
                    # Top right corner case
                    elif j == 5:
                        if board[i][j - 1] == ' ' or board[i + 1][j] == ' ' or board[i + 1][j - 1] == ' ':
                            return True
                    # Rest of top edge
                    else:
                        if board[i][j - 1] == ' ' or board[i][j + 1] == ' ' or board[i + 1][j - 1] == ' ' or board[i + 1][j] == ' ' or board[i + 1][j + 1] == ' ':
                            return True
                # Bottom edge
                elif i == 5:
                    # Bottom left corner case
                    if j == 0:
                        if board[i][j + 1] == ' ' or board[i - 1][j] == ' ' or board[i - 1][j + 1] == ' ':
                            return True
                    # Bottom right corner case
                    elif j == 5:
                        if board[i][j - 1] == ' ' or board[i - 1][j] == ' ' or board[i - 1][j - 1] == ' ':
                            return True
                    # Rest of bottom edge
                    else:
                        if board[i][j - 1] == ' ' or board[i][j + 1] == ' ' or board[i - 1][j - 1] == ' ' or board[i - 1][j] == ' ' or board[i - 1][j + 1] == ' ':
                            return True
                # Left edge
                elif j == 0:
                    # Making sure to not do corners
                    if i != 0 and i != 5:
                        if board[i - 1][j + 1] == ' ' or board[i][j + 1] == ' ' or board[i + 1][j + 1] == ' ' or board[i - 1][j] == ' ' or board[i + 1][j] == ' ':
                            return True
                # Right edge
                elif j == 5:
                    # Making sure to not do corners
                    if i != 0 and i != 5:
                        if board[i - 1][j - 1] == ' ' or board[i][j - 1] == ' ' or board[i + 1][j - 1] == ' ' or board[i - 1][j] == ' ' or board[i + 1][j] == ' ':
                            return True
                # Rest of board
                else:
                    # Should be 8 total conditionals as there are 8 bordering squares
                    if board[i - 1][j - 1] == ' ' or board[i][j - 1] == ' ' or board[i + 1][j - 1] == ' ':
                        return True
                    if board[i - 1][j] == ' ' or board[i + 1][j] == ' ':
                        return True
                    if board[i - 1][j + 1] == ' ' or board[i][j + 1] == ' ' or board[i + 1][j + 1] == ' ':
                        return True
    return False


# Checking if offense can make the move
def check_legal(board, player, i, j):
    if i == 0:
        # Literal top left corner case
        if j == 0:
            if board[i][j + 1] == player.name or board[i + 1][j] == player.name or board[i + 1][j + 1] == player.name:
                return True
        # Top right corner case
        elif j == 5:
            if board[i][j - 1] == player.name or board[i + 1][j] == player.name or board[i + 1][j - 1] == player.name:
                return True
        # Rest of top edge
        else:
            if board[i][j - 1] == player.name or board[i][j + 1] == player.name or board[i + 1][j - 1] == player.name or board[i + 1][j] == player.name or board[i + 1][j + 1] == player.name:
                return True
    # Bottom edge
    elif i == 5:
        # Bottom left corner case
        if j == 0:
            if board[i][j + 1] == player.name or board[i - 1][j] == player.name or board[i - 1][j + 1] == player.name:
                return True
        # Bottom right corner case
        elif j == 5:
            if board[i][j - 1] == player.name or board[i - 1][j] == player.name or board[i - 1][j - 1] == player.name:
                return True
        # Rest of bottom edge
        else:
            if board[i][j - 1] == player.name or board[i][j + 1] == player.name or board[i - 1][j - 1] == player.name or board[i - 1][j] == player.name or board[i - 1][j + 1] == player.name:
                return True
    # Left edge
    elif j == 0:
        # Making sure to not do corners
        if i != 0 and i != 5:
            if board[i - 1][j + 1] == player.name or board[i][j + 1] == player.name or board[i + 1][j + 1] == player.name or board[i - 1][j] == player.name or board[i + 1][j] == player.name:
                return True
    # Right edge
    elif j == 5:
        # Making sure to not do corners
        if i != 0 and i != 5:
            if board[i - 1][j - 1] == player.name or board[i][j - 1] == player.name or board[i + 1][j - 1] == player.name or board[i - 1][j] == player.name or board[i + 1][j] == player.name:
                return True
    # Rest of board
    else:
        # Should be 8 total conditionals as there are 8 bordering squares
        if board[i - 1][j - 1] == player.name or board[i][j - 1] == player.name or board[i + 1][j - 1] == player.name:
            return True
        if board[i - 1][j] == player.name or board[i + 1][j] == player.name:
            return True
        if board[i - 1][j + 1] == player.name or board[i][j + 1] == player.name or board[i + 1][j + 1] == player.name:
            return True
    return False


# Playing a move and checking if it's legal
def play_move(board, player, firstMove):
    while True:
        try:
            move = input(player.name + "'s Move: ")
            # Forcing input to be in 'a-1' format
            if re.search(r"^[a-fA-F][1-6]$", move):
                # Converting so I can index
                j = move[0].lower()
                i = move[1]
                i = 5 - int(i) + 1
                j = letter_to_num[j]
                if board[i][j] == ' ':
                    # If defense, then move is legal
                    if player.team == 'defense':
                        board[i][j] = player.name
                    elif firstMove is True:
                        board[i][j] = player.name
                        firstMove = False
                    else:
                        # Checking if the move is adjacent for offense
                        if check_legal(board, player, i, j) is True:
                            board[i][j] = player.name
                        else:
                            raise ValueError
                else:
                    raise ValueError
                break
            else:
                raise TypeError
        # Letting them retry until they put in a valid move
        except ValueError:
            print("Invalid Move")
            pass
        except TypeError:
            print("Format: letternumber")
            pass


# Checking score everytime a move is player
def check_score(board, player, player2):
    # Resetting player score
    player.score = 0
    # Splitting this into horizontal, vertical, four corners, and illuminati
    horizontal_check(board, player)
    vertical_check(board, player)
    diagonal_check_1(board, player)
    diagonal_check_2(board, player)
    four_corners_check(board, player)
    illuminati_check(board, player, player2)


# Horizontal check
def horizontal_check(board, player):
    for i in range(6):
        connect = 0
        # Start at middle because without those squares there is no possible way to score
        if board[i][2] == player.name and board[i][3] == player.name:
            connect = 2
            if board[i][1] == player.name:
                connect += 1
                if board[i][0] == player.name:
                    connect += 1
            if board[i][4] == player.name:
                connect += 1
                if board[i][5] == player.name:
                    connect += 1
        # Scoring
        if connect >= 6:
            player.score += 5
        elif connect >= 5:
            player.score += 2
        elif connect >= 4:
            player.score += 1


# Vertical Check
def vertical_check(board, player):
    for i in range(6):
        connect = 0
        # Start at middle as well because without those squares there is no possible way to score
        if board[2][i] == player.name and board[3][i] == player.name:
            connect = 2
            if board[1][i] == player.name:
                connect += 1
                if board[0][i] == player.name:
                    connect += 1
            if board[4][i] == player.name:
                connect += 1
                if board[5][i] == player.name:
                    connect += 1
        # Scoring
        if connect >= 6:
            player.score += 5
        elif connect >= 5:
            player.score += 2
        elif connect >= 4:
            player.score += 1


# Diagonal Check for top left to bottom right
def diagonal_check_1(board, player):
    # Range 5 because the last square can't be this diagonal
    for i in range(5):
        connect = 0
        # Top left to Bottom right diagonals
        if board[2][i] == player.name:
            connect = 1
            # Making sure element index exists
            if 0 <= i + 1 <= 5:
                if board[3][i + 1] == player.name:
                    connect += 1
                    if 0 <= i + 2 <= 5:
                        if board[4][i + 2] == player.name:
                            connect += 1
                        if 0 <= i + 3 <= 5:
                            if board[5][i + 3] == player.name:
                                connect += 1
                    if 0 <= i - 1 <= 5:
                        if board[1][i - 1] == player.name:
                            connect += 1
                            if 0 <= i - 2 <= 5:
                                if board[0][i - 2] == player.name:
                                    connect += 1
        # Scoring
        if connect >= 6:
            player.score += 5
        elif connect >= 5:
            player.score += 2
        elif connect >= 4:
            player.score += 1


# Diagonal Check for top right to bottom left
def diagonal_check_2(board, player):
    # Range 5 again for the same reason
    for i in range(5):
        connect = 0
        # Top left to Bottom right diagonals
        if board[3][i] == player.name:
            connect = 1
            # Making sure element index exists
            if 0 <= i + 1 <= 5:
                if board[2][i + 1] == player.name:
                    connect += 1
                    if 0 <= i + 2 <= 5:
                        if board[1][i + 2] == player.name:
                            connect += 1
                        if 0 <= i + 3 <= 5:
                            if board[0][i + 3] == player.name:
                                connect += 1
                    if 0 <= i - 1 <= 5:
                        if board[4][i - 1] == player.name:
                            connect += 1
                            if 0 <= i - 2 <= 5:
                                if board[5][i - 2] == player.name:
                                    connect += 1
        # Scoring
        if connect >= 6:
            player.score += 5
        elif connect >= 5:
            player.score += 2
        elif connect >= 4:
            player.score += 1


# Four Corners
def four_corners_check(board, player):
    # Just check if the player has all 4 corners
    if board[0][0] == player.name:
        if board[0][5] == player.name:
            if board[5][0] == player.name:
                if board[5][5] == player.name:
                    player.score += 1


def illuminati_check(board, player, player2):
    for i in range(6):
        for j in range(6):
            if board[i][j] == player.name:
                # Checking if vertex can be top left triangle
                if 0 <= i - 3 and 0 <= j - 3:
                    # Vertical Check
                    if board[i - 1][j] == player.name and board[i - 2][j] == player.name and board[i - 3][j] == player.name:
                        # Horizontal Check
                        if board[i][j - 1] == player.name and board[i][j - 2] == player.name and board[i][j - 3] == player.name:
                            # Diagonal Check and if it's surrounding an opposing mark
                            if board[i - 2][j - 1] == player.name and board[i - 1][j - 2] == player.name and board[i - 1][j - 1] == player2.name:
                                player.score += 1
                # Checking if vertex can be top right triangle
                elif 0 <= i - 3 and 5 >= j + 3:
                    # Vertical Check
                    if board[i - 1][j] == player.name and board[i - 2][j] == player.name and board[i - 3][j] == player.name:
                        # Horizontal Check
                        if board[i][j + 1] == player.name and board[i][j + 2] == player.name and board[i][j + 3] == player.name:
                            # Diagonal Check and if it's surrounding an opposing mark
                            if board[i - 2][j + 1] == player.name and board[i - 1][j + 2] == player.name and board[i - 1][j + 1] == player2.name:
                                player.score += 3
                # Checking if vertex can be bottom left triangle
                elif 5 >= i + 3 and 0 <= j - 3:
                    # Vertical Check
                    if board[i + 1][j] == player.name and board[i + 2][j] == player.name and board[i + 3][j] == player2.name:
                        # Horizontal Check
                        if board[i][j - 1] == player.name and board[i][j - 2] == player.name and board[i][j - 3] == player.name:
                            # Diagonal Check and if it's surrounding an opposing mark
                            if board[i + 2][j - 1] == player.name and board[i + 1][j - 2] == player.name and board[i + 1][j - 1] == player2.name:
                                player.score += 3
                # Checking if vertex can be bottom right triangle
                elif 5 >= i - 3 and 5 >= j + 3:
                    # Vertical Check
                    if board[i + 1][j] == player.name and board[i + 2][j] == player.name and board[i + 3][j] == player.name:
                        # Horizontal Check
                        if board[i][j + 1] == player.name and board[i][j + 2] == player.name and board[i][j + 3] == player.name:
                            # Diagonal Check and if it's surrounding an opposing mark
                            if board[i + 2][j + 1] == player.name and board[i + 1][j + 2] == player.name and board[i + 1][j + 1] == player2.name:
                                player.score += 3


def end_game(board, p1, p2):
    for i in range(6):
        for j in range(6):
            if board[i][j] != p1.name:
                board[i][j] = p2.name
    check_score(board, p1, p2)
    check_score(board, p2, p1)
    print_board(board, p1, p2)
    sys.exit()


if __name__ == "__main__":
    main()
