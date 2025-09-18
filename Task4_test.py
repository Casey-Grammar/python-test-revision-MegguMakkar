import unittest
from unittest.mock import patch
import io
import sys
import task4

class TestTask4(unittest.TestCase):
    
    @patch('builtins.input', return_value='Open sesame!')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_correct_password(self, mock_stdout, mock_input):
        """Test with correct password 'Open sesame!'"""
        task4.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "The cave door opens!")
    
    @patch('builtins.input', return_value='open sesame!')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_incorrect_case(self, mock_stdout, mock_input):
        """Test with incorrect case 'open sesame!'"""
        task4.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "")
    
    @patch('builtins.input', return_value='Open Sesame!')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_incorrect_capitalization(self, mock_stdout, mock_input):
        """Test with incorrect capitalization 'Open Sesame!'"""
        task4.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "")
    
    @patch('builtins.input', return_value='wrong password')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_wrong_password(self, mock_stdout, mock_input):
        """Test with completely wrong password"""
        task4.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "")
    
    @patch('builtins.input', return_value='Open sesame')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_missing_exclamation(self, mock_stdout, mock_input):
        """Test with 'Open sesame' (missing exclamation mark)"""
        task4.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "")

if __name__ == '__main__':
    unittest.main()