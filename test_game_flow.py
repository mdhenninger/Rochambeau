import unittest
from unittest.mock import patch
import builtins
import io
import sys
import rochambeau

class TestRochambeauGameFlow(unittest.TestCase):
    def print_test_summary(self, test_name, output, passed):
        print(f"\n--- Test: {test_name} ---")
        print("Result:", "PASS" if passed else "FAIL")
        print("Captured Output:")
        print(output[:1000] + ("..." if len(output) > 1000 else ""))
        print("-------------------------\n")

    @patch('builtins.input', side_effect=['rock', '4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_one_round_and_exit(self, mock_stdout, mock_input):
        # Patch get_computer_choice to always return 'scissors' so player wins
        with patch('rochambeau.get_computer_choice', return_value='scissors'):
            rochambeau.main()
        output = mock_stdout.getvalue()
        try:
            self.assertIn('You chose: rock', output)
            self.assertIn('Computer chose: scissors', output)
            self.assertIn('YOU WIN', output.upper())
            self.assertIn('Thanks for playing!', output)
            passed = True
        except AssertionError:
            passed = False
        self.print_test_summary('test_play_one_round_and_exit', output, passed)
        if not passed:
            raise

    @patch('builtins.input', side_effect=['2', '1', '4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_multiple_rounds(self, mock_stdout, mock_input):
        # Patch get_computer_choice to alternate between 'rock' and 'scissors'
        with patch('rochambeau.get_computer_choice', side_effect=['rock', 'scissors']):
            rochambeau.main()
        output = mock_stdout.getvalue()
        try:
            self.assertIn('You chose: paper', output)
            self.assertIn('Computer chose: rock', output)
            self.assertIn('YOU WIN', output.upper())
            self.assertIn('You chose: rock', output)
            self.assertIn('Computer chose: scissors', output)
            self.assertIn('YOU WIN', output.upper())
            self.assertIn('Thanks for playing!', output)
            passed = True
        except AssertionError:
            passed = False
        self.print_test_summary('test_play_multiple_rounds', output, passed)
        if not passed:
            raise

    @patch('builtins.input', side_effect=[
        'r', 'p', 's', '1', '2', '3',
        'invalid', 'rock', '4'
    ])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_all_valid_and_invalid_selections(self, mock_stdout, mock_input):
        # Computer always picks 'rock' for simplicity
        with patch('rochambeau.get_computer_choice', return_value='rock'):
            rochambeau.main()
        output = mock_stdout.getvalue()
        try:
            # Check all valid selections
            self.assertIn('You chose: rock', output)
            self.assertIn('You chose: paper', output)
            self.assertIn('You chose: scissors', output)
            # Check number selections
            self.assertIn('You chose: rock', output)
            self.assertIn('You chose: paper', output)
            self.assertIn('You chose: scissors', output)
            # Check invalid selection handling
            self.assertIn('Invalid choice. Please try again.', output)
            self.assertIn('Thanks for playing!', output)
            passed = True
        except AssertionError:
            passed = False
        self.print_test_summary('test_all_valid_and_invalid_selections', output, passed)
        if not passed:
            raise

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestRochambeauGameFlow)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print(f"\n========== TEST SUMMARY ==========")
    print(f"Total tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"==================================\n")
