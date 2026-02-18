from typing import Callable
from app.operations.operations import add, subtract, multiply, divide

class Calculation:
     
    def __init__(self, a: float, b: float, operation: Callable):
        self.a = a
        self.b = b
        self.operation = operation

    def execute(self) -> float:
        return self.operation(self.a, self.b)

    def __str__(self) -> str:
        return f"{self.operation.__name__}({self.a}, {self.b}) = {self.execute()}"


class CalculationFactory:
    
    _operations = {
        "add":      add,
        "subtract": subtract,
        "multiply": multiply,
        "divide":   divide,
    }

    @classmethod
    def create(cls, operation_name: str, a: float, b: float) -> Calculation:
        if operation_name not in cls._operations:
            raise ValueError(f"Unknown operation: '{operation_name}'. "
                             f"Choose from: {list(cls._operations.keys())}")
        return Calculation(a, b, cls._operations[operation_name])