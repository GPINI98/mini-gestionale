class Dipendente:
    def __init__(self, nome, eta, stipendio):
        self.nome = nome
        self.eta = eta
        self.__stipendio = stipendio


    def presenta(self):
        print(
            f"{self.nome}, {self.eta}, {self.__stipendio}"
            )

    def aumenta_stipendio(self, aumento):
        if aumento > 0:
            self.__stipendio += aumento
            return True
        else:
            return False

    def calcola_stipendio_annuo(self):
        return self.__stipendio * 12

    def descrizione(self):
        return f"il dipendente {self.nome} ha {self.eta} anni e guadagna {self.__stipendio} euro al mese"

    def aumento_stipendio_percentuale(self, percentuale):
        if percentuale > 0:
            aumento = self.__stipendio * (percentuale / 100)
            self.__stipendio += aumento
            return True
        else:
            return False

    def get_stipendio(self):
        return self.__stipendio

dipendente1 = Dipendente("Mario", 30, 2500)
dipendente2 = Dipendente("Luca", 25, 500)
dipendente1.presenta()
dipendente2.presenta()
stipendio_annuo1 = dipendente1.calcola_stipendio_annuo()
print(f"Lo stipendio annuo di {dipendente1.nome} è: {stipendio_annuo1}")

print(dipendente1.descrizione())
print(dipendente2.descrizione())

dipendente1.aumento_stipendio_percentuale(-10)
# print(f"Dopo l'aumento, lo stipendio di {dipendente1.nome} è: {dipendente1.__stipendio}")

stipendio = dipendente1.get_stipendio()
print(stipendio)  # Accesso al metodo get_stipendio per ottenere lo stipendio
  # Accesso al metodo get_stipendio per ottenere lo stipendio

dipendente1.aumenta_stipendio(-500)
print(f"Dopo l'aumento, lo stipendio di {dipendente1.nome} è: {dipendente1.get_stipendio()}")
