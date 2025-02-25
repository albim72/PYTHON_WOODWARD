from resistor import Resistor

class BoundedResistance(Resistor):
    def __init__(self,ohms):
        super().__init__(ohms)
        
    @property
    def ohms(self):
        return self._ohms
    
    @ohms.setter
    def ohms(self,ohms):
        if ohms <= 0:
            raise ValueError("Wartość oproności nie może być ujemna lub równa zero!")
        self._ohms = ohms
