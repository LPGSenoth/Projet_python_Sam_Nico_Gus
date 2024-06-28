import Equipe
import Championnat

equipe_0 = Equipe('Basket','rennes', ('toto', 'riri', 'fifi', 'loulou', 'lulu'))
equipe_1 = Equipe('Basket','vannes', ('chloé', 'pierre', 'valentine', 'claudia', 'luc'))
equipe_2 = Equipe('Basket','nantes', ('marc', 'manu', 'maher', 'benoit', 'leandro'))
equipe_3 = Equipe('Basket','brest', ('estelle', 'luca', 'mathis', 'clémentine', 'yann'))

equipe_0Vsequipe_1 = (40, 31)
equipe_0Vsequipe_2 = (40, 39)
equipe_0Vsequipe_3 = (40, 40)
equipe_1Vsequipe_0 = (45, 40)
equipe_1Vsequipe_2 = (34, 56)
equipe_1Vsequipe_3 = (49, 41)
equipe_2Vsequipe_0 = (40, 31)
equipe_2Vsequipe_1 = (40, 39)
equipe_2Vsequipe_3 = (40, 40)
equipe_3Vsequipe_0 = (45, 40)
equipe_3Vsequipe_1 = (34, 56)
equipe_3Vsequipe_2 = (49, 41)

c = Championnat()
c.add_all_teams(equipe_0, equipe_1, equipe_2, equipe_3)
c.show_all_teams()
c.affichage()
for i in range(4):
    for j in range(4):
        if i != j:
            s = 'equipe_' + str(i) + 'Vsequipe_' + str(j)
            c.add_games(s, eval(s))

c.affichage()
c.show_points()
c.show_ranking()
c.calculate_points()
c.show_points()
c.create_classement()
c.show_ranking()
