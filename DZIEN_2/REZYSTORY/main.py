from oldresistor import OldResistor
from resistor import Resistor

print("_________ klasa OldResistor __________")
r0 = OldResistor(10.2E3)
print(r0)
print(r0.get_ohms())
r0.set_ohms(2.88E+2)
print(r0.get_ohms())

print("_________ klasa Resistor __________")
r1 = Resistor(5E3)
r1.ohms = 18.3
print(f'układ elektryczny: {r1.ohms} omów\n'
      f'napięcie elektryczne: {r1.voltage} V\n'
      f'natężenie prądu: {r1.current} A\n')
