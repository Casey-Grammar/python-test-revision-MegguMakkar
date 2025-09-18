import unittest
from unittest.mock import patch
import io
import sys
import task10

class TestTask10(unittest.TestCase):
    
    @patch('builtins.input', return_value='John Mary Peter Susan')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_already_capitalized_names(self, mock_stdout, mock_input):
        """Test with names that are already properly capitalized"""
        task10.main()
        expected_output = "Class Roll\nJohn\nMary\nPeter\nSusan"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    @patch('builtins.input', return_value='john mary peter susan')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_lowercase_names(self, mock_stdout, mock_input):
        """Test with all lowercase names"""
        task10.main()
        expected_output = "Class Roll\nJohn\nMary\nPeter\nSusan"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    @patch('builtins.input', return_value='JOHN MARY PETER SUSAN')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_uppercase_names(self, mock_stdout, mock_input):
        """Test with all uppercase names"""
        task10.main()
        expected_output = "Class Roll\nJohn\nMary\nPeter\nSusan"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    @patch('builtins.input', return_value='John mary PETER susan')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mixed_case_names(self, mock_stdout, mock_input):
        """Test with mixed case names"""
        task10.main()
        expected_output = "Class Roll\nJohn\nMary\nPeter\nSusan"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    @patch('builtins.input', return_value='Zack Bob Alice David')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sorting(self, mock_stdout, mock_input):
        """Test that names are properly sorted alphabetically"""
        task10.main()
        expected_output = "Class Roll\nAlice\nBob\nDavid\nZack"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_input(self, mock_stdout, mock_input):
        """Test with empty input"""
        task10.main()
        expected_output = "Class Roll"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    @patch('builtins.input', return_value='john-paul mary-kate robert jr.')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hyphenated_names(self, mock_stdout, mock_input):
        """Test with hyphenated and multiple-word names"""
        task10.main()
        expected_output = "Class Roll\nJohn-paul\nJr.\nMary-kate\nRobert"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    @patch('builtins.input', return_value='  Alice   Bob  Carol  ')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_extra_spaces(self, mock_stdout, mock_input):
        """Test with extra spaces between names"""
        task10.main()
        expected_output = "Class Roll\nAlice\nBob\nCarol"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()