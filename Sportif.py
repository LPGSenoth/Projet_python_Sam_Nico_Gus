from  Personne import Personne


class Sportif(Personne):
    def __init__(self,name,sport,age=None):
        Personne.__init__(self,name,age)
        self.sport = sport

    def get_sport(self):
        return self.sport

    def affiche(self):
        print(f"Nom: {self.name}, Sport: {self.sport}")

