import unittest


'''
Математические операции функциями:
one(plus(two())) == 3
'''


def handle_operation(number: float, operation):
    if operation:
        return operation(number)

    return number


def zero(operation = None):
    return handle_operation(0, operation)


def one(operation = None):
    return handle_operation(1, operation)


def two(operation = None):
    return handle_operation(2, operation)


def three(operation = None):
    return handle_operation(3, operation)


def four(operation = None):
    return handle_operation(4, operation)


def five(operation = None):
    return handle_operation(5, operation)


def six(operation = None):
    return handle_operation(6, operation)


def seven(operation = None):
    return handle_operation(7, operation)


def eight(operation = None):
    return handle_operation(8, operation)


def nine(operation = None):
    return handle_operation(9, operation)


##  math operators
def plus(arg):
    return lambda number: number + arg


def minus(arg):
    return lambda number: number - arg


def multiplied_by(arg):
    return lambda number: number * arg


def divided_by(arg):
    if arg == 0:
        raise ZeroDivisionError
    return lambda number: number / arg
## -------------


class TestFunctions(unittest.TestCase):
    def test_one_plus_two(self) -> None:
        self.assertEqual(one(plus(two())), 3)

    def test_two_multiplied_by_three(self) -> None:
        self.assertEqual(two(multiplied_by(three())), 6)

    def test_two_divided_by_two(self) -> None:
        self.assertEqual(two(divided_by(two())), 1)

    def test_two_minus_two(self) -> None:
        self.assertEqual(two(minus(two())), 0)

    def test_two_divided_by_zero(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            two(divided_by(zero()))


def main() -> None:
    pass


def test() -> None:
    unittest.main()


if __name__ == '__main__':
    test()
