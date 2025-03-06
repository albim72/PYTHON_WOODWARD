from typing import Protocol, List, Callable, Generator


# Definicja protokołu do odczytu danych
class FileReaderProtocol(Protocol):
    def read_line_by_line(self) -> Generator[str, None, None]:
        ...

    def read_in_blocks(self, block_size: int) -> Generator[List[str], None, None]:
        ...

    def read_with_filter(self, filter_function: Callable[[str], bool]) -> Generator[str, None, None]:
        ...


# Implementacja klasy korzystającej z protokołu
class TextFileReader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_line_by_line(self) -> Generator[str, None, None]:
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                yield line.strip()

    def read_in_blocks(self, block_size: int) -> Generator[List[str], None, None]:
        with open(self.file_path, 'r',encoding='utf-8') as file:
            block = []
            for line in file:
                block.append(line.strip())
                if len(block) >= block_size:
                    yield block
                    block = []
            if block:
                yield block

    def read_with_filter(self, filter_function: Callable[[str], bool]) -> Generator[str, None, None]:
        with open(self.file_path, 'r',encoding='utf-8') as file:
            for line in file:
                stripped_line = line.strip()
                if filter_function(stripped_line):
                    yield stripped_line


# Przykładowe użycie
if __name__ == "__main__":
    # Utworzenie instancji czytnika pliku
    reader = TextFileReader("example.txt")

    print("Odczyt wiersz po wierszu:")
    for line in reader.read_line_by_line():
        print(line)

    print("\nOdczyt blokami (po 3 linie):")
    for block in reader.read_in_blocks(3):
        print(block)

    print("\nOdczyt z filtracją (linie zawierające słowo 'Python'):")
    for filtered_line in reader.read_with_filter(lambda x: "Python" in x):
        print(filtered_line)
