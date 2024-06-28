Le but du programme est d’implémenter le résultat d’un championnat de sport.
Les différentes classes expliquées ci-dessous sont à implémenter. 
Vous pouvez écrire toutes les classes dans un fichier ou dans des fichiers séparés selon votre convenance.

• Une personne qui a un nom et un âge. Par défaut, âge est égal à None. Dans le programme de test, on ne fournira pas d’âge
• Un sportif, qui est une personne mais qui a un attribut sport en plus.
La méthode affiche permet également d’afficher le nom du sportif.
• Les équipes sont composées de sportifs. La classe Equipe est construite avec 3 arguments
  o Sport qui décrit le sport pratiqué (‘basket’ dans notre exemple)
  o Nom de l’équipe
  o Un tuple avec tous les joueurs de l’équipe.
  
Les 4 équipes du championnat sont donc créées ainsi :
equipe_0 = Equipe('Basket','rennes', ('toto', 'riri', 'fifi', 'loulou', 'lulu'))
equipe_1 = Equipe('Basket','vannes', ('chloé', 'pierre', 'valentine', 'claudia', 'luc'))
equipe_2 = Equipe('Basket','nantes', ('marc', 'manu', 'maher', 'benoit', 'leandro'))
equipe_3 = Equipe('Basket','brest', ('estelle', 'luca', 'mathis', 'clémentine', 'yann'))
