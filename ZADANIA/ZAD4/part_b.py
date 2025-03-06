from typing import Callable, Dict


# Klasa obsługująca dynamiczne dodawanie i wykonywanie funkcji
class DynamicFunctionHandler:
    def __init__(self):
        self.functions: Dict[str, Callable] = {}

    def add_function(self, name: str, function: Callable) -> None:
        """Dodaje nową funkcję o podanej nazwie."""
        self.functions[name] = function
        print(f"Funkcja '{name}' została dodana.")

    def remove_function(self, name: str) -> None:
        """Usuwa funkcję o podanej nazwie."""
        if name in self.functions:
            del self.functions[name]
            print(f"Funkcja '{name}' została usunięta.")
        else:
            print(f"Funkcja '{name}' nie istnieje.")

    def execute_function(self, name: str, *args, **kwargs):
        """Wykonuje funkcję o podanej nazwie z argumentami."""
        if name in self.functions:
            print(f"Wywoływanie funkcji '{name}'...")
            return self.functions[name](*args, **kwargs)
        else:
            print(f"Funkcja '{name}' nie została znaleziona.")
            return None


# Przykładowe użycie
if __name__ == "__main__":
    # Utworzenie instancji klasy DynamicFunctionHandler
    handler = DynamicFunctionHandler()

    # Definiowanie funkcji dynamicznych
    def greet(name: str):
        return f"Cześć, {name}!"

    def add_numbers(a: int, b: int):
        return a + b

    def multiply_numbers(a: int, b: int):
        return a * b

    # Dodawanie funkcji do handlera
    handler.add_function("greet", greet)
    handler.add_function("add", add_numbers)
    handler.add_function("multiply", multiply_numbers)

    # Wykonywanie funkcji
    print(handler.execute_function("greet", "Anna"))
    print(handler.execute_function("add", 5, 10))
    print(handler.execute_function("multiply", 3, 4))

    # Usuwanie funkcji
    handler.remove_function("add")

    # Próba wykonania usuniętej funkcji
    handler.execute_function("add", 5, 10)
