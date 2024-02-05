import unittest 
from Rock_Paper_Scissors import Winner, user1, user2

class TestWinnerFunction(unittest.TestCase):
    
    def test_winner_tie(self):
        result = Winner("ROCK", "ROCK", user1, user2)
        self.assertEqual(result, "It's a tie!")

    def test_winner_player1_wins(self):
        result = Winner("ROCK", "SCISSORS", user1, user2)
        self.assertEqual(result, "ROCK wins!\nCongratulations, " + user1 + "!")

    def test_winner_player2_wins(self):
        result = Winner("SCISSORS", "ROCK", user1, user2)
        self.assertIn("ROCK wins!", result)
        self.assertIn("Congratulations, " + user2 + "!", result)

if __name__ == '__main__':
    unittest.main()