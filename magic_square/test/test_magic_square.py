import pytest
from unittest import TestCase
from hackerank.magic_square.magic_square import sum_row, sum_columns, sum_diagonal, verify, select_magic_constant


@pytest.mark.parametrize("test_input,expected",
                         [([[1, 2, 4]], [7]),
                          ([[1, 2, 4], [1, 2, 4], [1, 2, 4], [1, 2, 4]], [7, 7, 7, 7]),
                          ([[1, 0, 3], [4, 5, 4], [1, 3, 4], [1, 2, 4]], [4, 13, 8, 7]),
                          ([[1, 2, 4], [1, 2, 4], [1, 2, 4]], [7, 7, 7]),
                          ([[1, 2, 4, 5], [1, 2, 4, 5], [1, 2, 4, 5], [1, 2, 4, 5]], [12, 12, 12, 12]),
                          ([[1, 0, 3, 4], [4, 5, 4, 9], [1, 3, 4, 8], [1, 2, 4, 7]], [8, 22, 16, 14]),
                          ([[4, 9, 2], [3, 5, 7], [8, 1, 5]], [15, 15, 14]),  # caso malo 1
                          ([[4, 9, 2], [3, 5, 7], [8, 1, 6]], [15, 15, 15]),  # caso bueno 1
                          ([[4, 8, 2], [4, 5, 7], [6, 1, 6]], [14, 16, 13]),  # caso malo 2
                          ([[4, 9, 2], [3, 5, 7], [8, 1, 6]], [15, 15, 15])  # caso bueno 2
                          ])
def test_sum_row(test_input, expected):
    assert sum_row(test_input) == expected


@pytest.mark.parametrize("test_input,expected",
                         [([[1, 2, 4]], [1, 2, 4]),
                          ([[1, 2, 4], [1, 2, 4], [1, 2, 4], [1, 2, 4]], [4, 8, 16]),
                          ([[1, 0, 3], [4, 5, 4], [1, 3, 4], [1, 2, 4]], [7, 10, 15]),
                          ([[1, 2, 4], [1, 2, 4], [1, 2, 4]], [3, 6, 12]),
                          ([[1, 2, 4, 5], [1, 2, 4, 5], [1, 2, 4, 5], [1, 2, 4, 5]], [4, 8, 16, 20]),
                          ([[1, 0, 3, 4], [4, 5, 4, 9], [1, 3, 4, 8], [1, 2, 4, 7]], [7, 10, 15, 28]),
                          ([[4, 9, 2], [3, 5, 7], [8, 1, 5]], [15, 15, 14]),  # caso malo 1
                          ([[4, 9, 2], [3, 5, 7], [8, 1, 6]], [15, 15, 15]),  # caso bueno 1
                          ([[4, 8, 2], [4, 5, 7], [6, 1, 6]], [14, 14, 15]),  # caso malo 2
                          ([[4, 9, 2], [3, 5, 7], [8, 1, 6]], [15, 15, 15])  # caso bueno 2
                          ])
def test_sum_column(test_input, expected):
    assert sum_columns(test_input) == expected


@pytest.mark.parametrize("test_input,expected",
                         [([[1, 2, 4], [1, 2, 4], [1, 2, 4]], [7, 7]),
                          ([[1, 2, 4, 5], [1, 2, 4, 5], [1, 2, 4, 5], [1, 2, 4, 5]], [12, 12]),
                          ([[1, 0, 3, 4], [4, 5, 4, 9], [1, 3, 4, 8], [1, 2, 4, 7]], [17, 12]),
                          ([[4, 9, 2], [3, 5, 7], [8, 1, 5]], [14, 15]),  # caso malo 1
                          ([[4, 9, 2], [3, 5, 7], [8, 1, 6]], [15, 15]),  # caso bueno 1
                          ([[4, 8, 2], [4, 5, 7], [6, 1, 6]], [15, 13]),  # caso malo 2
                          ([[4, 9, 2], [3, 5, 7], [8, 1, 6]], [15, 15])  # caso bueno 2
                          ])
def test_sum_diagonal(test_input, expected):
    assert sum_diagonal(test_input) == expected


@pytest.mark.parametrize("test_input,expected",
                         [([[1, 2, 4], [1, 2, 4], [1, 2, 4]], (False, {3, 6, 7, 12})),
                          ([[1, 2, 4, 5], [1, 2, 4, 5], [1, 2, 4, 5], [1, 2, 4, 5]], (False, {12, 4, 8, 16, 20})),
                          ([[1, 0, 3, 4], [4, 5, 4, 9], [1, 3, 4, 8], [1, 2, 4, 7]],
                           (False, {8, 22, 16, 14, 17, 12, 7, 10, 15, 28})),
                          ([[4, 9, 2], [3, 5, 7], [8, 1, 5]], (False, {14, 15})),  # caso malo 1
                          ([[4, 9, 2], [3, 5, 7], [8, 1, 6]], (True, {15})),  # caso bueno 1
                          ([[4, 8, 2], [4, 5, 7], [6, 1, 6]], (False, {13, 14, 15, 16})),  # caso malo 2
                          ([[4, 9, 2], [3, 5, 7], [8, 1, 6]], (True, {15}))  # caso bueno 2
                          ])
def test_verify(test_input, expected):
    assert verify(test_input) == expected


@pytest.mark.parametrize("test_input,expected",
                         [  # ([[1, 2, 4], [1, 2, 4], [1, 2, 4]], 7),
                             # ([[1, 2, 4, 5], [1, 2, 4, 5], [1, 2, 4, 5], [1, 2, 4, 5]], 12),
                             # ([[1, 0, 3, 4], [4, 5, 4, 9], [1, 3, 4, 8], [1, 2, 4, 7]], 8),
                             (([15, 15, 14], [15, 15, 14], [14, 15], (False, {14, 15})), 15),  # caso malo 1
                             (([15, 15, 15], [15, 15, 15], [15, 15], (True, {15})), 15),  # caso bueno 1
                             (([14, 16, 13], [14, 14, 15], [15, 13], (False, {13, 14, 15, 16})), 14),  # caso malo 2
                             (([15, 15, 15], [15, 15, 15], [15, 15], (True, {15})), 15)  # caso bueno 2
                         ])
def test_select_magic_constant(test_input, expected):
    assert select_magic_constant(*test_input) == expected


class MagicSquareTest(TestCase):

    def setUp(self) -> None:
        with open("/Users/mgamez/Documents/Pluralsight/hackerank/magic_square/test/test_case.txt") as file:
            s = file.read()
        self.s = list(map(lambda x: list(map(int, x.split())), s.split('\n')))
