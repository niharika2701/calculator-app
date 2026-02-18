import pytest
from unittest.mock import patch, MagicMock
from app.calculator.calculator import Calculator


class TestCalculator:

    def setup_method(self):
        self.calc = Calculator()

    def test_initial_history_is_empty(self):
        assert self.calc.get_history() == []

    def test_perform_calculation_add(self):
        result = self.calc.perform_calculation("add", 5, 3)
        assert result == 8

    def test_perform_calculation_subtract(self):
        result = self.calc.perform_calculation("subtract", 10, 4)
        assert result == 6

    def test_perform_calculation_multiply(self):
        result = self.calc.perform_calculation("multiply", 3, 7)
        assert result == 21

    def test_perform_calculation_divide(self):
        result = self.calc.perform_calculation("divide", 20, 5)
        assert result == 4.0

    def test_perform_calculation_stores_history(self):
        self.calc.perform_calculation("add", 1, 2)
        self.calc.perform_calculation("multiply", 3, 4)
        assert len(self.calc.get_history()) == 2

    def test_perform_calculation_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.perform_calculation("divide", 5, 0)

    def test_perform_calculation_unknown_operation(self):
        with pytest.raises(ValueError, match="Unknown operation"):
            self.calc.perform_calculation("power", 2, 3)

    def test_get_history_returns_string_representations(self):
        self.calc.perform_calculation("add", 2, 3)
        history = self.calc.get_history()
        assert len(history) == 1
        assert "add" in history[0]

    
    def test_repl_exit_command(self):
        with patch("builtins.input", return_value="exit"):
            with patch("builtins.print") as mock_print:
                self.calc.run()
        printed = " ".join(str(c) for c in mock_print.call_args_list)
        assert "exit" in printed.lower() or "goodbye" in printed.lower() or "bye" in printed.lower()

    def test_repl_help_command(self, capsys):
        with patch("builtins.input", side_effect=["help", "exit"]):
            self.calc.run()
        captured = capsys.readouterr()
        assert "add" in captured.out.lower() or "operation" in captured.out.lower()

    def test_repl_history_command_empty(self, capsys):
        with patch("builtins.input", side_effect=["history", "exit"]):
            self.calc.run()
        captured = capsys.readouterr()
        assert "no history" in captured.out.lower() or "empty" in captured.out.lower()

    def test_repl_history_command_with_entries(self, capsys):
        self.calc.perform_calculation("add", 1, 2)
        with patch("builtins.input", side_effect=["history", "exit"]):
            self.calc.run()
        captured = capsys.readouterr()
        assert "add" in captured.out

    def test_repl_valid_calculation(self, capsys):
        with patch("builtins.input", side_effect=["add 5 3", "exit"]):
            self.calc.run()
        captured = capsys.readouterr()
        assert "8" in captured.out

    def test_repl_invalid_number_input(self, capsys):
        with patch("builtins.input", side_effect=["add five 3", "exit"]):
            self.calc.run()
        captured = capsys.readouterr()
        assert "invalid" in captured.out.lower() or "error" in captured.out.lower()

    def test_repl_wrong_number_of_arguments(self, capsys):
        with patch("builtins.input", side_effect=["add 5", "exit"]):
            self.calc.run()
        captured = capsys.readouterr()
        assert "invalid" in captured.out.lower() or "error" in captured.out.lower()

    def test_repl_unknown_operation(self, capsys):
        with patch("builtins.input", side_effect=["power 2 3", "exit"]):
            self.calc.run()
        captured = capsys.readouterr()
        assert "unknown" in captured.out.lower() or "error" in captured.out.lower()

    def test_repl_divide_by_zero(self, capsys):
        with patch("builtins.input", side_effect=["divide 10 0", "exit"]):
            self.calc.run()
        captured = capsys.readouterr()
        assert "zero" in captured.out.lower() or "error" in captured.out.lower()