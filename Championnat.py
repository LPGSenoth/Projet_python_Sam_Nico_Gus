#IMPORT EQUIPE

class Championnat:
    def __init__(self):
        self.results = []
        self.Teams = []
        self.Points = {}
        self.Classement = {}

    def init_championnat(self):
        self.results = [[None for _ in range(4)] for _ in range(4)]
        self.Points = {team: 0 for team in ['equipe_0', 'equipe_1', 'equipe_2', 'equipe_3']}
        self.Classement = {rank: None for rank in ['1', '2', '3', '4']}
    
    def add_all_teams(self, teams):
        self.Teams = teams

    def show_all_teams(self):
        return self.Teams

c = Championnat()
c.add_all_teams(['equipe_0', 'equipe_1', 'equipe_2', 'equipe_3'])
c.init_championnat()
print(c.results)
print(c.Points)
print(c.Classement)