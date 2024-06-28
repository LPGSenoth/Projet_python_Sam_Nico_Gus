import Personne


class Sportif(Personne):
    def __init__(self,nom,age,sport):
        Personne.__init__(self,nom,age)
        self.sport = sport

    def get_sport(self):
        return self.sport

    def affiche(self):
        print(f"le nom du sportif ou sportive est {self.nom}")

    