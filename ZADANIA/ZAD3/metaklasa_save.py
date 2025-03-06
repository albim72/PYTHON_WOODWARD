# Definiujemy metaklasę, która zapisuje atrybuty i metody klasy do pliku
class SaveToFileMeta(type):
    def __new__(cls, name, bases, dct):
        # Tworzymy nazwę pliku na podstawie nazwy klasy
        filename = f"{name}_attributes.txt"

        # Otwieramy plik do zapisu
        with open(filename, 'w') as f:
            # Zapisujemy nazwę klasy
            f.write(f"Class name: {name}\n\n")

            # Zapisujemy atrybuty klasy (zmienne oraz metody)
            f.write("Attributes and Methods:\n")
            for attribute_name, attribute_value in dct.items():
                if callable(attribute_value):
                    # Jeżeli atrybut jest metodą, zapisujemy ją jako metodę
                    f.write(f"Method: {attribute_name}\n")
                else:
                    # Jeżeli atrybut jest zmienną, zapisujemy ją jako zmienną
                    f.write(f"Attribute: {attribute_name}\n")

        # Tworzymy klasę przy użyciu nadpisanej metaklasy
        return super().__new__(cls, name, bases, dct)


# Przykładowa klasa, która używa metaklasy SaveToFileMeta
class ExampleClass(metaclass=SaveToFileMeta):
    # Atrybuty klasy
    variable1 = "Hello"
    variable2 = "World"

    # Metody klasy
    def method1(self):
        return f"{self.variable1} {self.variable2}"

    def method2(self):
        return self.variable1.lower()



class MClass(metaclass=SaveToFileMeta):
    e:int = 90
    f:float = 0.8778
    h:bool = True

    def calc(self,x,y):
        return x+2*y

    def info(self,i):
        return 5*i


# Utworzenie klasy spowoduje zapisanie jej atrybutów i metod do pliku
example = ExampleClass()

# Otwórz plik i sprawdź zawartość
with open('ExampleClass_attributes.txt', 'r') as file:
    print(file.read())

mc = MClass()


