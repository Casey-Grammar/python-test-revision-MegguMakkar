import unittest
from unittest.mock import patch
import io
import sys
import task7

class TestTask7(unittest.TestCase):
    
    @patch('builtins.input', return_value='5')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_countdown_from_five(self, mock_stdout, mock_input):
        """Test countdown from 5"""
        task7.main()
        expected_output = "Counting down ...\n5 ...\n4 ...\n3 ...\n2 ...\n1 ...\nBlast off!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_countdown_from_one(self, mock_stdout, mock_input):
        """Test countdown from 1"""
        task7.main()
        expected_output = "Counting down ...\n1 ...\nBlast off!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    @patch('builtins.input', return_value='10')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_countdown_from_ten(self, mock_stdout, mock_input):
        """Test countdown from 10"""
        task7.main()
        expected_output = "Counting down ...\n10 ...\n9 ...\n8 ...\n7 ...\n6 ...\n5 ...\n4 ...\n3 ...\n2 ...\n1 ...\nBlast off!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    @patch('builtins.input', return_value='0')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_countdown_from_zero(self, mock_stdout, mock_input):
        """Test countdown from 0 - should immediately blast off with no countdown"""
        task7.main()
        expected_output = "Counting down ...\nBlast off!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    @patch('builtins.input', return_value='-5')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_countdown_from_negative(self, mock_stdout, mock_input):
        """Test countdown from negative number - should immediately blast off with no countdown"""
        task7.main()
        expected_output = "Counting down ...\nBlast off!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    @patch('builtins.input', side_effect=['abc', '3'])
    def test_invalid_input_handling(self, mock_input):
        """Test handling of non-integer input"""
        with self.assertRaises(ValueError):
            task7.main()

if __name__ == '__main__':
    unittest.main()