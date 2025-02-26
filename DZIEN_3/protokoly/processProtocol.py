from typing import Protocol,List,Any
import numpy as np

class DataProcessor(Protocol):
    def process(self,data:List[Any])->List[Any]:
        pass

class NumberProcessor:
    def process(self,data:List[Any])->List[Any]:
        return [item*2 for item in data if isinstance(item,int) or isinstance(item,float)]

class StringProcessor:
    def process(self, data: List[Any]) -> List[Any]:
        return [item.upper() for item in data if isinstance(item,str)]

#funkcja przyjmująca obiekt zgodny z protokołem DataProcessor
def process_data(processor:DataProcessor,data:List[Any]) -> List[Any]:
    return processor.process(data)

number_processor = NumberProcessor()
string_processor = StringProcessor()

data_to_process = [1,2,"ok",3,4,5,6,6.78,0.53,"hej","zielony",78.5,"456","r",[3,6,"coś"]]
array_tonp = [4,7,4,6,3,78,3,"tak",63,678,33,5,4.44,"nie"]
array_mix = np.array(array_tonp)
# array_tonp = np.array(array_tonp,dtype=float)
print(array_tonp)
print(type(array_tonp))

proc_nb = process_data(number_processor,data_to_process)
proc_str = process_data(string_processor,data_to_process)

print(f'wynik dla liczb: {proc_nb}')
print(f'wynik dla tesktu: {proc_str}')

print(f"TEST DLA NUMPY")

proc_nbnp = process_data(number_processor,array_tonp)
proc_strnp = process_data(string_processor,array_tonp)

print(f'wynik dla liczb - numpy: {proc_nbnp}')
print(f'wynik dla tesktu - numpy: {proc_strnp}')
