import unittest
from unittest.mock import patch
import io
import sys
import task5

class TestTask5(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['3', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_italy_wins(self, mock_stdout, mock_input):
        """Test when Italy has a higher score than Brazil"""
        task5.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Italy won the match.")
    
    @patch('builtins.input', side_effect=['1', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_brazil_wins(self, mock_stdout, mock_input):
        """Test when Brazil has a higher score than Italy"""
        task5.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Brazil won the match.")
    
    @patch('builtins.input', side_effect=['2', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_draw(self, mock_stdout, mock_input):
        """Test when both teams have the same score"""
        task5.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "The match was a draw.")
    
    @patch('builtins.input', side_effect=['0', '0'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_scoreless_draw(self, mock_stdout, mock_input):
        """Test when both teams score 0"""
        task5.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "The match was a draw.")
    
    @patch('builtins.input', side_effect=['10', '5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_high_scores(self, mock_stdout, mock_input):
        """Test with higher scores"""
        task5.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Italy won the match.")
    
    @patch('builtins.input', side_effect=['5', '10'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_high_scores_brazil_wins(self, mock_stdout, mock_input):
        """Test with higher scores, Brazil wins"""
        task5.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Brazil won the match.")
    
    @patch('builtins.input', side_effect=['11', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two_digit_vs_one_digit(self, mock_stdout, mock_input):
        """Test comparison with different length scores - now with integer comparison"""
        task5.main()
        # With int conversion, 11 is correctly greater than 2
        self.assertEqual(mock_stdout.getvalue().strip(), "Italy won the match.")
    
    @patch('builtins.input', side_effect=['abc', '2'])
    def test_invalid_input(self, mock_input):
        """Test handling of non-numeric input"""
        with self.assertRaises(ValueError):
            task5.main()
    
    @patch('builtins.input', side_effect=['2', 'abc'])
    def test_invalid_second_input(self, mock_input):
        """Test handling of non-numeric input for the second score"""
        with self.assertRaises(ValueError):
            task5.main()

if __name__ == '__main__':
    unittest.main()