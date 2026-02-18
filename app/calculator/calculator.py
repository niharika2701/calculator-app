from app.calculation.calculation import CalculationFactory

class Calculator:
    HELP_TEXT = "add, subtract, multiply, divide - operations available"

    def __init__(self):
        self._history: list=[]

    def perform_calculation(self, operation: str, a: float, b: float) -> float:
        calc = CalculationFactory.create(operation, a, b)
        result = calc.execute()
        self._history.append(calc)
        return result
    
    def get_history(self) -> list:
        return [str(c) for c in self._history]
    
    def _parse_input(self, user_input: str):
        parts = user_input.strip().split()

        if len(parts) == 1 and parts[0] in ("exit", "help", "history"):
            return parts[0]
        if len(parts) != 3:
            raise ValueError(
                f"Invalid format. Expected: <operation> <num1> <num2>. Got: '{user_input}'"
            )
        operation, raw_a, raw_b = parts
        
        try:
            a = float(raw_a)
            b = float(raw_b)
        except ValueError:
            raise ValueError(f"Invalid numbers: '{raw_a}' and '{raw_b}' must be numeric.")

        return operation, a, b
    
    def _handle_command(self, command: str) -> bool:
        
        if command == "exit":
            print("Goodbye! Thanks for using the calculator.")
            return True
        if command == "help":
            print(self.HELP_TEXT)
        if command == "history":
            history = self.get_history()
            if not history:
                print("No history yet. Perform a calculation first!")
            else:
                print("\nCalculation History:")
                for i, entry in enumerate(history, 1):
                    print(f" {i}. {entry}")
        return False
    
    def run(self):  
        print("Welcome to the Professional Calculator!")
        print("Type 'help' for instructions or 'exit' to quit.\n")
        self._repl_loop()
    
    def _repl_loop(self):
        while True:
            try:
                user_input=input("calc>").strip()

                if not user_input:
                    continue # pragma: no cover

                parsed=self._parse_input(user_input)

                if isinstance(parsed, str):
                    should_exit=self._handle_command(parsed)
                    if should_exit:
                        break
                    continue
                
                operation, a, b=parsed

                try:
                    result=self.perform_calculation(operation, a, b)
                    print(f"Result: {result}")
                except ValueError as e:
                    print(f"Error: {e}")
                
            except ValueError as e:
                print(f"Error: {e}")
            except EOFError:  # pragma: no cover
                print("\nGoodbye!")
                break