import unittest
from unittest.mock import patch
import io
import sys
import task9

class TestTask9(unittest.TestCase):
    
    @patch('builtins.input', return_value='Whiskers Mittens Fluffy')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three_cats(self, mock_stdout, mock_input):
        """Test with three cat names"""
        task9.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "You have 3 cats.")
    
    @patch('builtins.input', return_value='Felix')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one_cat(self, mock_stdout, mock_input):
        """Test with one cat name"""
        task9.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "You have 1 cats.")
    
    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_no_cats(self, mock_stdout, mock_input):
        """Test with empty input (no cats)"""
        task9.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "You have 0 cats.")
    
    @patch('builtins.input', return_value='Whiskers Mittens Fluffy Felix Smokey Tiger Luna Simba Oliver Leo Bella Nala Max Chloe')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_many_cats(self, mock_stdout, mock_input):
        """Test with many cat names"""
        task9.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "You have 14 cats.")
    
    @patch('builtins.input', return_value='   Whiskers    Mittens   Fluffy   ')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_extra_spaces(self, mock_stdout, mock_input):
        """Test with extra spaces between names"""
        task9.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "You have 3 cats.")
    
    @patch('builtins.input', return_value='  ')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_only_spaces(self, mock_stdout, mock_input):
        """Test with only spaces input"""
        task9.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "You have 0 cats.")

if __name__ == '__main__':
    unittest.main()