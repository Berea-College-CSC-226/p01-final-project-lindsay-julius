# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#
#
# if __name__ == '__main__':
#     unittest.main()

from inspect import getframeinfo, stack

from Character import *

def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """

    # caller = getframeinfo(stack()[1][0])
    # linenum = caller.lineno
    self.number_of_aces =

    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)




