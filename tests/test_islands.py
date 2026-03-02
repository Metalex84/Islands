import pytest
from island_counter import parse_board, count_islands
from exceptions import InvalidBoardFormat


def test_empty_board():
    with pytest.raises(InvalidBoardFormat):
        parse_board([])


def test_non_rectangular():
    with pytest.raises(InvalidBoardFormat):
        parse_board(["10", "101"])


def test_invalid_character():
    with pytest.raises(InvalidBoardFormat):
        parse_board(["10a", "101"])


def test_all_water():
    board = parse_board(["000", "000"])
    assert count_islands(board) == 0


def test_all_land():
    board = parse_board(["111", "111"])
    assert count_islands(board) == 1


def test_multiple_islands():
    board = parse_board([
        "11000",
        "11010",
        "00100",
        "00011",
    ])
    assert count_islands(board) == 1  # diagonales conectan todo


def test_single_cell_island():
    board = parse_board(["1"])
    assert count_islands(board) == 1


def test_single_cell_water():
    board = parse_board(["0"])
    assert count_islands(board) == 0