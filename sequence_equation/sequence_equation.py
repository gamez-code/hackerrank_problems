import unittest


def permutationEquation(p):
    result = list()
    for x in range(1, len(p) + 1):
        result.append(p.index(p.index(x) + 1) + 1)
    else:
        return result


"""
class PermutationEquationTest(unittest.TestCase):

    def test_permutation_equation(self):
        p = '4 3 5 1 2'
        p = list(map(int, p.split()))
        result = permutationEquation(p)

        assert (result == [1, 3, 5, 4, 2])
"""

if __name__ == '__main__':
    p = '4 3 5 1 2'
    p = list(map(int, p.split()))
    print(permutationEquation(p))
