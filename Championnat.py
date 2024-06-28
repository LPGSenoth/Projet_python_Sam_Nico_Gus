#IMPORT EQUIPE

class Championnat:
    def __init__(self):
        self.results = []
        self.Teams = []
        self.Points = {}
        self.Classement = {}

    def init_championnat(self):
        self.results = [[None for _ in range(4)] for _ in range(4)]
        self.Points = {team: 0 for team in self.Teams}
        self.Classement = {rank: None for rank in ['1', '2', '3', '4']}
    
    def add_all_teams(self, teams):
        self.Teams = teams

    def show_all_teams(self):
        for team in self.Teams:
            team.show_team_name()
    
    def add_game(self, teams, score):
        team1, team2 = teams.split('V')
        self.results[self.Teams.index(team1)][self.Teams.index(team2)] = score
    
    def calculate_points(self):
        for i in range(4):
            for j in range(4):
                if self.results[i][j] is not None:
                    if self.results[i][j][0] > self.results[i][j][1]:
                        self.Points[self.Teams[i]] += 3
                    elif self.results[i][j][0] == self.results[i][j][1]:
                        self.Points[self.Teams[i]] += 1
                        self.Points[self.Teams[j]] += 1
                    else:
                        self.Points[self.Teams[j]] += 3


c = Championnat()
c.add_all_teams(['equipe_0', 'equipe_1', 'equipe_2', 'equipe_3'])
c.init_championnat()
print(c.results)
print(c.Points)
print(c.Classement)
c.add_game('equipe_0Vequipe_1', (2, 1))
c.add_game('equipe_0Vequipe_2', (5, 1))
c.add_game('equipe_1Vequipe_2', (1, 1))
c.add_game('equipe_1Vequipe_3', (0, 1))
c.add_game('equipe_2Vequipe_0', (2, 1))
c.add_game('equipe_2Vequipe_1', (2, 1))
c.add_game('equipe_3Vequipe_2', (2, 1))
c.add_game('equipe_3Vequipe_0', (2, 1))
print(c.results)
c.calculate_points()
print(c.Points)
