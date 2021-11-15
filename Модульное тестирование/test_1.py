"""Почему тест test_log завершается с ошибкой?"""

import unittest
from unittest.mock import patch
from io import StringIO


def summ(a, b):
    print("summ({}, {})".format(a, b))
    res = a + b
    return res


class MainTest(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_log(self, mock_stdout):
        summ(1, 3)
        self.assertEqual(mock_stdout.getvalue(), 'summ(1, 3)')


if __name__ == '__main__':
    unittest.main()
