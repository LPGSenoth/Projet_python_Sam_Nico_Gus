from  Sportif import Sportif

class Equipe:
    def __init__(self,sport,name,equipe_members):
        self.name = name
        self.sport = sport
        self.equipe_members = [Sportif(nom,sport) for nom in equipe_members]

    def show_team_name(self):
        print(f" l'equipe de {self.name} est constitué des joueurs suivants : ")


    def show_team_players(self):
        for membre in self.equipe_members:
            membre.affiche()




euuqipe = Equipe('basket','paris',('joueur1','joueur2','joueur3','joueur4','joueur5'))

euuqipe.show_team_players()