class ContextManager:
    def __init__(self):
        print("wywołanie funkcji init()\ndefinicja obiektu Context Manager")

    def __enter__(self):
        print("wywołanie funkcji enter\nprzekazanie kontekstu do instrukcji with [wymagane]")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("wywołanie funkcji exit\nzamknięcie obiektu Context Managera [wymagane]")

with ContextManager() as manager:
    print("wykonanie bloku with...")
