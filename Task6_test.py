import unittest
from unittest.mock import patch
import io
import sys
import task6

class TestTask6(unittest.TestCase):
    
    @patch('builtins.input', return_value='I saw a bear in the woods')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_bear_present(self, mock_stdout, mock_input):
        """Test when 'bear' is present in the input"""
        task6.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "There's a bear in there.")
    
    @patch('builtins.input', return_value='There are no animals here')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_no_bear(self, mock_stdout, mock_input):
        """Test when 'bear' is not present in the input"""
        task6.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "No bears here.")
    
    @patch('builtins.input', return_value='bear')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_only_bear(self, mock_stdout, mock_input):
        """Test when the input is just the word 'bear'"""
        task6.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "There's a bear in there.")
    
    @patch('builtins.input', return_value='The teddy bear is on the shelf')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_bear_as_part_of_word(self, mock_stdout, mock_input):
        """Test when 'bear' is part of a longer word"""
        task6.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "There's a bear in there.")
    
    @patch('builtins.input', return_value='Bears are dangerous')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_bears_plural(self, mock_stdout, mock_input):
        """Test when 'bears' (plural) is in the input, which contains 'bear'"""
        task6.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "There's a bear in there.")
    
    @patch('builtins.input', return_value='be ar')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_bear_with_space(self, mock_stdout, mock_input):
        """Test when 'bear' is split by a space"""
        task6.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "No bears here.")
    
    @patch('builtins.input', return_value='BEAR')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_uppercase_bear(self, mock_stdout, mock_input):
        """Test with uppercase 'BEAR' - should not match due to case sensitivity"""
        task6.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "No bears here.")
    
    @patch('builtins.input', return_value='bearly visible')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_bear_at_start_of_word(self, mock_stdout, mock_input):
        """Test when 'bear' is at the start of a longer word"""
        task6.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "There's a bear in there.")
    
    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_input(self, mock_stdout, mock_input):
        """Test with empty input"""
        task6.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "No bears here.")

if __name__ == '__main__':
    unittest.main()