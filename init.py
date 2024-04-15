from utilisateurs.utilisateur_dao import UtilisateurDao
#from utilisateur import Utilisateur

utilisateur_dao = UtilisateurDao()
message = utilisateur_dao.add_utilisateur('Bijou', 'tresor', '35', 'bij@test.com', '12345', 'Admin')

print(message)