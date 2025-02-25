from trojkat import Trojkat
from prostokat import Prostokat
from trapez import Trapez
from kolo import Kolo

"""
Komentarz dokumentacyjny
xyz
"""

tr = Trojkat(5.6,7.8)
print(f"pole figury {tr.__class__.__name__} wynosi: {tr.policz_pole():.2f} cm2")

pr1 = Prostokat(7.3,3.9)
print(f"pole figury {pr1.__class__.__name__} wynosi: {pr1.policz_pole():.2f} cm2")
print(type(pr1))

pr2 = Prostokat(5,5)
print(f"pole figury {pr2.__class__.__name__} wynosi: {pr2.policz_pole():.2f} cm2")
print(type(pr2))

trp = Trapez(7.6,5.7,4.4)
print(f"pole figury {trp.__class__.__name__} wynosi: {trp.policz_pole():.2f} cm2")

kl = Kolo(6.6)
print(f"pole figury {kl.__class__.__name__} wynosi: {kl.policz_pole():.2f} cm2")
