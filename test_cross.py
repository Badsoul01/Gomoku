import pytest
from cross_OPP import Board


def test_win_horizontal():
    """Testuje, zda hra pozná 5 symbolů v řadě vodorovně"""

    b= Board(10)
    for c in range(5):
        b.make_move(0,c,"X")

    winner, coords = b.checking_winning()
    assert winner == "X"
    assert len(coords) == 5
    # Ověříme konkrétní souřadnice vítězství
    assert coords == [(0,0),(0,1),(0,2),(0,3),(0,4)]

def test_win_vertical():
    """Testuje, zda hra pozná 5 symbolů pod sebou."""
    b = Board(10)
    # Nasimulujeme 5 "O" pod sebou
    for r in range(5):
        b.make_move(0,r,"O")

    winner, coords = b.checking_winning()
    assert winner == "O"
    assert len(coords) == 5

def test_move_on_occupied_squere():
    b = Board(5)
    b.make_move(2,2,"X")
    result =b.make_move(2,2,"O")

    assert result is False #Metoda musí vrátit False
    assert b.rows[2][2]  == "X" # Na políčku musí zůstat původní X
    