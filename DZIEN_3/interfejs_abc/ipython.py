from abc import ABCMeta,abstractmethod

class IPojazd(metaclass=ABCMeta):
    @abstractmethod
    def spalanie(self,odl,jedn):raise NotImplementedError

    @abstractmethod
    def koszt_przejazdu(self,jedn,cena_jedn):raise NotImplementedError
