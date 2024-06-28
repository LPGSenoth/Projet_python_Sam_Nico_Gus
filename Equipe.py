from  Sportif import Sportif

class Equipe:
    def __init__(self,sport,name,equipe_members):
        self.name = name
        self.sport = sport
        for nom in equipe_members :
            self.equipe_member = [Sportif]

    def show_team_name(self):
        print(f" l'equipe de {self.name} est constitué des joueurs suivants : ")


    def show_team_players(self):
        for membre in self.equipe_members:
            joueur = Sportif(membre)
            joueur.affiche()




euuqipe = Equipe('basket','paris',(joueur1,joueur2,joueur3,joueur4,joueur5))

euuqipe.show_team_players()