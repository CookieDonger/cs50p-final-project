import project


def test_Player():
    p1 = project.Player('A', 'offense')
    p2 = project.Player('B', 'defense')
    assert p1.name == 'A'
    assert p2.name == 'B'
    assert p1.team == 'offense'
    assert p2.team == 'defense'


def test_create_board():
    board = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    assert project.create_board() == board


def test_get_name(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'A')
    result = project.get_name()
    assert result == 'A'
    inputs = iter(['HI', 'd'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = project.get_name()
    assert result == 'd'
    inputs = iter(['nDoihd', '9', 'g'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = project.get_name()
    assert result == 'g'


def test_check_possible():
    p1 = project.Player('a', 'offense')
    board = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 'a', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    assert project.check_possible(board, p1) is True
    board2 = [['a', 'a', 'b', ' ', ' ', ' '], [' ', 'b', 'a', 'b', ' ', ' '], [' ', 'b', 'a', 'a', ' ', ' '], [' ', 'b', 'a', 'a', ' ', 'b'], [' ', ' ', 'b', 'a', 'b', ' '], ['b', ' ', 'b', 'b', 'a', 'a']]
    assert project.check_possible(board, p1) is True
    board3 = [['a', 'b', ' ', ' ', ' ', ' '], ['b', 'b', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    assert project.check_possible(board3, p1) is False
    board4 = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', 'b', 'b', 'b', ' ', ' '], [' ', 'b', 'a', 'b', ' ', ' '], [' ', 'b', 'b', 'b', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    assert project.check_possible(board4, p1) is False


def test_check_legal():
    p1 = project.Player('a', 'offense')
    board = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    assert project.check_legal(board, p1, 2, 2) is False
    board = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 'a', 'a', ' ', ' '], [' ', ' ', ' ', 'b', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    assert project.check_legal(board, p1, 5, 1) is False
    board = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 'a', 'b', ' ', ' '], [' ', 'b', 'a', 'a', ' ', ' '], [' ', ' ', ' ', ' ', 'a', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    assert project.check_legal(board, p1, 0, 0) is False
    board = [[' ', ' ', ' ', ' ', ' ', ' '], ['a', 'a', ' ', 'b', ' ', ' '], [' ', 'b', 'a', 'a', ' ', ' '], [' ', ' ', ' ', 'b', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    assert project.check_legal(board, p1, 0, 0) is True


def test_play_move(monkeypatch):
    p1 = project.Player('a', 'offense')
    p2 = project.Player('b', 'defense')
    board = project.create_board()
    inputs = iter(['A1', 'A2', 'D4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    project.play_move(board, p1, True)
    project.play_move(board, p1, False)
    project.play_move(board, p2, False)
    assert board[5][0] == 'a'
    assert board[4][0] == 'a'
    assert board[2][3] == 'b'


def test_check_score():
    p1 = project.Player('A', 'offense')
    p2 = project.Player('B', 'defense')
    board = [['B', 'A', 'B', 'A', 'A', 'B'], ['B', 'A', 'A', 'A', 'A', 'B'], ['B', 'A', 'A', 'B', 'A', 'B'], ['B', 'A', 'A', 'A', 'A', 'B'], ['B', 'B', 'A', 'A', 'A', 'B'], ['B', 'A', 'B', 'B', 'A', 'B']]
    project.check_score(board, p1, p2)
    project.check_score(board, p2, p1)
    assert p1.score == 19
    assert p2.score == 11


def