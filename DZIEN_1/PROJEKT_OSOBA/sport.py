class Sport:
    def __init__(self,dyscyplina,lataupr,bestwynik):
        self.dyscyplina = dyscyplina
        self.lataupr = lataupr
        self.bestwynik = bestwynik
        
    def infosport(self):
        return f"dyscyplina sportowa - {self.dyscyplina}, lata uprawiania: {self.lataupr}, życiówka: {self.bestwynik}"
