import unittest , Character , Player


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.player = Character.Character()


    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here

    def test_ace_logic_directly(self):
        self.player.number_of_aces = 1
        self.player.card_values = 11
        self.assertEqual(self.player.number_of_aces, 1, "Ace count should be 1")
        self.assertEqual(self.player.card_values, 11, "Value should be 11")

        self.player.number_of_aces = 1
        self.player.card_values = 20

        self.player.card_picker()
        self.assertEqual(self.player.card_values, self.player.card + 20 - 10)



if __name__ == '__main__':
    unittest.main()




