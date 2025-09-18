import unittest
from unittest.mock import patch
import io
import sys
import task2

class TestTask2(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['James', 'Bond'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_james_bond(self, mock_stdout, mock_input):
        """Test main function with first name 'James' and last name 'Bond'"""
        task2.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "My name is Bond, James Bond")
        
    @patch('builtins.input', side_effect=['John', 'Doe'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_john_doe(self, mock_stdout, mock_input):
        """Test main function with first name 'John' and last name 'Doe'"""
        task2.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "My name is Doe, John Doe")
        
    @patch('builtins.input', side_effect=['', ''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_empty_inputs(self, mock_stdout, mock_input):
        """Test main function with empty inputs"""
        task2.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "My name is ,")
        
    @patch('builtins.input', side_effect=['Ada', 'Lovelace'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_ada_lovelace(self, mock_stdout, mock_input):
        """Test main function with first name 'Ada' and last name 'Lovelace'"""
        task2.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "My name is Lovelace, Ada Lovelace")
    
    @patch('builtins.input', side_effect=['Special@Name', 'Last-Name'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_special_characters(self, mock_stdout, mock_input):
        """Test main function with names containing special characters"""
        task2.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "My name is Last-Name, Special@Name Last-Name")

if __name__ == '__main__':
    unittest.main()