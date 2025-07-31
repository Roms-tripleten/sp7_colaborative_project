import argparse

class Calculator:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.memory = 0  # Atributo nuevo para guardar resultados

    def add(self, a, b):
        result = a + b
        if self.verbose:
            print(f"🧮 Adding {a} + {b} = {result}")
        else:
            print(result)
        self.memory = result

    def operate(self, operation=None, numbers=None):
        if not operation or not numbers:
            print("⚠️ No operation or numbers provided.")
            return

        a, b = numbers
        if operation == "add":
            self.add(a, b)
        elif operation == "subtract":
            self.substract(a, b)
        elif operation == "multiply":
            self.multiply(a, b)
        elif operation == "divide":
            self.divide(a, b)    
        else:
            print(f"🚧 Operation '{operation}' not implemented yet.")

    def substract(self,a,b):
        result = a - b
        if self.verbose:
            print(f"🧮 Subtracting {a} - {b} = {result}")
        else:
            print(result)
        self.memory = result    
    
    def multiply(self,a,b):
        result = a * b
        if self.verbose:
            print(f"🧮 Multiplying {a} * {b} = {result}")
        else:
            print(result)
        self.memory = result

    def divide(self,a,b):
        if b == 0:
            print("🚫 Error: Division by zero is not allowed.")
            return
        result = a / b
        if self.verbose:
            print(f"🧮 Dividing {a} / {b} = {result}")
        else:
            print(result)
        self.memory = result
    ## Opcional
    def show_memory(self):
        if self.memory:
            print(f"🧠 Memory: {self.memory}")
        else:
            print("🧠 Memory is empty.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mini Calculator CLI")
    parser.add_argument("--verbose", action="store_true", help="Show detailed output")
    parser.add_argument("--operation", type=str, choices=["add", "subtract", "multiply", "divide"], help="Math operation to perform")
    parser.add_argument("--numbers", nargs=2, type=float, help="Two numbers to operate with")
    parser.add_argument("--memory", action="store_true", help="Show memory")
    args = parser.parse_args()

    calc = Calculator(verbose=args.verbose)
    if args.memory:
        calc.show_memory()
    else:
        calc.operate(operation=args.operation, numbers=args.numbers)
