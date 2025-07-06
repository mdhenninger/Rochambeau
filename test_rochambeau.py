import unittest
from rochambeau import determine_winner, get_ascii_art

class TestDetermineWinner(unittest.TestCase):
    def test_tie(self):
        self.assertEqual(determine_winner('rock', 'rock'), "It's a tie!")
        self.assertEqual(determine_winner('paper', 'paper'), "It's a tie!")
        self.assertEqual(determine_winner('scissors', 'scissors'), "It's a tie!")

    def test_player_wins(self):
        self.assertIn("YOU WIN", determine_winner('rock', 'scissors').upper())
        self.assertIn("YOU WIN", determine_winner('paper', 'rock').upper())
        self.assertIn("YOU WIN", determine_winner('scissors', 'paper').upper())

    def test_computer_wins(self):
        self.assertIn("COMPUTER WINS", determine_winner('rock', 'paper').upper())
        self.assertIn("COMPUTER WINS", determine_winner('paper', 'scissors').upper())
        self.assertIn("COMPUTER WINS", determine_winner('scissors', 'rock').upper())

class TestAsciiArt(unittest.TestCase):
    def test_ascii_art_rock(self):
        art = get_ascii_art('rock')
        self.assertIn('_____', art)
        self.assertIn('(___)', art)

    def test_ascii_art_paper(self):
        art = get_ascii_art('paper')
        self.assertIn('_____', art)
        self.assertIn('______)', art)

    def test_ascii_art_scissors(self):
        art = get_ascii_art('scissors')
        self.assertIn('_____', art)
        self.assertIn('(___)', art)

    def test_ascii_art_invalid(self):
        self.assertEqual(get_ascii_art('lizard'), '')
        self.assertEqual(get_ascii_art(''), '')
        self.assertEqual(get_ascii_art(None), '')

if __name__ == '__main__':
    unittest.main()
