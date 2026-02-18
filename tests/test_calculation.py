import pytest
from app.operations.operations import add, subtract, multiply, divide
from app.calculation.calculation import Calculation, CalculationFactory

class TestCalculation:
    
    def test_calculation_stores_operands_and_operations(self):
        calc=Calculation(5, 3, add)

        assert calc.a==5
        assert calc.b==3
        assert calc.operation==add
    
    def test_calculation_execute_add(self):

        calc=Calculation(5, 3, add)
        result=calc.execute()
        assert result==8
    
    def test_calculation_execute_subtract(self):

        calc=Calculation(10, 4, subtract)
        result=calc.execute()
        assert result==6
    
    def test_calculation_execute_multiply(self):

        calc=Calculation(3, 7, multiply)
        result=calc.execute()
        assert result==21
    
    def test_calculation_execute_divide(self):

        calc=Calculation(20, 4, divide)
        result=calc.execute()
        assert result==5.0
    
    def test_calculation_execute_divide_by_zero(self):

        calc=Calculation(5, 0, divide)
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.execute()
    
    def test_calculation_str_representation(self):
        calc = Calculation(5, 3, add)
        result = str(calc)
        assert "5" in result
        assert "3" in result
        assert "add" in result

class TestCalculationFactory:

    @pytest.mark.parametrize("operation_name, a, b, expected", [
        ("add", 5, 3, 8),
        ("subtract", 10, 4, 6),
        ("multiply", 3, 7, 21),
        ("divide", 20, 4, 5.0),
    ])

    def test_factory_creates_correct_calculation(self, operation_name, a, b, expected):
        calc=CalculationFactory.create(operation_name, a, b)
        assert calc.execute()==expected

    def test_factory_raises_on_unknown_operation(self):
        with pytest.raises(ValueError, match="Unknown operation"):
            CalculationFactory.create("modulo", 5, 3)






    
