from typing import Protocol,Union

class Convertible(Protocol):
    def convert(self,data:str) -> Union[int,float]:
        pass

#implementacja protokołu
class IntegerConverter:
    def convert(self,data:str)->int:
        return int(data)

class FloatConverter:
    def convert(self,data:str)->float:
        return float(data)

class BoolConverter:
    def convert(self,data:str)->bool:
        data = float(data)
        return bool(data)

def conver_data(converter:Convertible,data:str) -> Union[int,float]:
    return converter.convert(data)

int_conv = IntegerConverter()
flt_conv = FloatConverter()
bl_conv = BoolConverter()

res_int = conver_data(int_conv,"7865")
res_float = conver_data(flt_conv,"0.7675")
res_bool = conver_data(bl_conv,"1")
res_bool2 = conver_data(bl_conv,"0")

print(f'konwersja na int: {res_int} -> typ {type(res_int)}')
print(f'konwersja na float: {res_float} -> typ {type(res_float)}')
print(f'konwersja na bool: {res_bool} -> typ {type(res_bool)}')
print(f'konwersja na bool: {res_bool2} -> typ {type(res_bool)}')
