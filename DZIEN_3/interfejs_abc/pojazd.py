from ipojazd import IPojazd

class Pojazd(IPojazd):
    def spalanie(self, odl, jedn):
        return jedn*100/odl

    def koszt_przejazdu(self, jedn, cena_jedn):
        return jedn*cena_jedn
