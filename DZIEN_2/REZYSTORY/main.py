from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance
from bounded import BoundedResistance

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

print("_________ klasa VoltageResistance __________")
r2 = VoltageResistance(1E3)
print(f"natężenie początkowe prądu: {r2.current} A")
r2.voltage = 55
print(f"napięcie prądu: {r2.voltage} V")
print(f"natężenie prądu: {r2.current} A")

print("_________ klasa BoundedResistance __________")
try:
      r3 = BoundedResistance(1E2)
      print(f"opór początkowy: {r3.ohms} omów")
      r3.ohms = -10
      print(f'opór: {r3.ohms} omów')
except ValueError as ve:
      print(ve)
