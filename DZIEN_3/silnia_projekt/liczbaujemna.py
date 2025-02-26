class SilniaUjemna(Exception):
    def __init__(self,n):
        self.n = n

    def __str__(self):
        return (f"została zadana wartość n= {self.n}\n"
                f"Wartość agrumentu funkcji silnia nie może być ujemna!")