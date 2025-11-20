import unittest , Character , Player


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.player = Character


    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here

    def test_ace_logic_directly(self):

        self.assertEqual(self.player.number_of_aces, 1, "Ace count should be 1")
        self.assertEqual(self.player.card_values, 11, "Value should be 11")

if __name__ == '__main__':
    unittest.main()

# from inspect import getframeinfo, stack
#
# from Character import *
#
# def unittest(did_pass):
#     """
#     Print the result of a unit test.
#     :param did_pass: a boolean representing the test
#     :return: None
#     """
#
#     # caller = getframeinfo(stack()[1][0])
#     # linenum = caller.lineno
#     self.number_of_aces =
#
#     if did_pass:
#         msg = "Test at line {0} ok.".format(linenum)
#     else:
#         msg = ("Test at line {0} FAILED.".format(linenum))
#     print(msg)




