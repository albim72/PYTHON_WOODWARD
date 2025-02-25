from oldresistor import OldResistor

print("_________ klasa OldResistor __________")
r0 = OldResistor(10.2E3)
print(r0)
print(r0.get_ohms())
r0.set_ohms(2.88E+2)
print(r0.get_ohms())
