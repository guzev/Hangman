import unittest


from src.game import find_all_pos_in_word
from src.game import step_of_game
from src.game import change_chars_in_positions


class TestGame(unittest.TestCase):

    def test_list_init(self):
        """
        Test that function find_all_positions_in_word works correct
        :return: list of positions of letter in current word
        """
        self.assertEqual(find_all_pos_in_word("aaaa", 'a'), [0, 1, 2, 3])
        self.assertEqual(find_all_pos_in_word('', 'b'), [])

    def test_change_letters_in_positions(self):
        """
        Test that functions changs letters in certian positions
        :return: changed word
        """
        self.assertEqual(change_chars_in_positions('aaa',
                                                   [0, 1, 2], 'b'), 'bbb')

    def test_step_of_game(self):
        """
        Test that one choice of player works right
        :return: changed word
        """
#       enter the letter y
#       self.assertEqual(step_of_game('****', 'yeah'), 'y***')


if __name__ == '__main__':
    unittest.main()
